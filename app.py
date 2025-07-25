from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

# --- Muat SEMUA model dan preprocessor saat startup ---
MODELS = {
    'logistic_regression': joblib.load('model/logistic_regression_model.pkl'),
    'random_forest': joblib.load('model/random_forest_model.pkl'),
    'svm': joblib.load('model/svm_model.pkl'),
    'naive_bayes': joblib.load('model/naive_bayes_model.pkl'),
    'knn': joblib.load('model/knn_model.pkl'),
}

ENCODERS = {
    'flag': joblib.load('model/encoder_flag.pkl'),
    'protocol_type': joblib.load('model/encoder_protocol_type.pkl'),
    'service': joblib.load('model/encoder_service.pkl')
}
SCALER = joblib.load('model/scaler.pkl')

if not isinstance(ENCODERS['flag'], LabelEncoder):
    raise TypeError("Objek yang dimuat dari 'encoder_flag.pkl' bukan LabelEncoder yang diharapkan.")
if not isinstance(ENCODERS['protocol_type'], LabelEncoder):
    raise TypeError("Objek yang dimuat dari 'encoder_protocol_type.pkl' bukan LabelEncoder yang diharapkan.")
if not isinstance(ENCODERS['service'], LabelEncoder):
    raise TypeError("Objek yang dimuat dari 'encoder_service.pkl' bukan LabelEncoder yang diharapkan.")


REQUIRED_FEATURES = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'logged_in',
    'root_shell', 'su_attempted', 'num_file_creations', 'num_access_files',
    'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
    'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
    'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate'
]

def predict_new_data(new_data, selected_model):
    df = pd.DataFrame([new_data])

    categorical_features = ['flag', 'protocol_type', 'service']
    for col in categorical_features:
        if col in df.columns:
            value_to_encode = df[col].iloc[0]
            encoder = ENCODERS[col]
            if value_to_encode in encoder.classes_:
                df[col] = encoder.transform([value_to_encode])[0]
            else:
                print(f"Peringatan: Nilai '{col}' '{value_to_encode}' tidak dikenal oleh encoder. Menggunakan -1.")
                df[col] = -1
        else:
            print(f"Peringatan: Kolom '{col}' tidak ditemukan di data input. Mengisi dengan 0.")
            df[col] = 0

    for col in REQUIRED_FEATURES:
        if col not in df.columns:
            df[col] = 0
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        except Exception as e:
            print(f"Peringatan: Gagal mengonversi kolom '{col}' ke numerik: {e}. Mengisi dengan 0.")
            df[col] = 0

    df = df[REQUIRED_FEATURES]
    df_scaled = SCALER.transform(df)

    # Lakukan prediksi probabilitas
    proba_anomaly = 0.5 # Default fallback
    if hasattr(selected_model, 'predict_proba'):
        # predict_proba mengembalikan probabilitas untuk semua kelas.
        # Untuk klasifikasi biner, biasanya [prob_kelas_0, prob_kelas_1].
        # Kita ingin probabilitas kelas 1 (anomali).
        probabilities = selected_model.predict_proba(df_scaled)[0]
        proba_normal = probabilities[0]  # Probabilitas kelas 0 (Normal)
        proba_anomaly = probabilities[1] # Probabilitas kelas 1 (Anomali)
    else:
        print(f"Peringatan: Model {selected_model.__class__.__name__} tidak mendukung predict_proba. Mengembalikan probabilitas 0.5 untuk keduanya.")
        proba_normal = 0.5

    # Ambang batas prediksi (misal 0.4 atau 0.5 sesuai keinginan Anda)
    # Saya akan tetap menggunakan 0.4 seperti di kode awal Anda,
    # tetapi Anda bisa mengubahnya menjadi 0.5 jika ingin 50% menjadi normal.
    pred = int(proba_anomaly >= 0.4)

    return {
        'prediction': pred,
        'probability_anomaly': round(proba_anomaly, 4), # Mengubah nama kunci
        'probability_normal': round(proba_normal, 4)    # Menambahkan probabilitas normal
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    available_models = {key: key.replace('_', ' ').title() for key in MODELS.keys()}

    if request.method == 'POST':
        selected_model_name = request.form.get('model_selector')
        selected_model = MODELS.get(selected_model_name)

        if not selected_model:
            result = {'prediction': -1, 'message': "Model yang dipilih tidak valid."}
            return render_template('index.html', result=result, available_models=available_models)

        input_data = {}
        for key in REQUIRED_FEATURES:
            val = request.form.get(key)
            if key in ['protocol_type', 'flag', 'service']:
                input_data[key] = val
            else:
                try:
                    input_data[key] = float(val) if val else 0.0
                except ValueError:
                    input_data[key] = 0.0

        try:
            result = predict_new_data(input_data, selected_model)
            result['model_used'] = available_models.get(selected_model_name, selected_model_name)
        except Exception as e:
            result = {'prediction': -1, 'message': f"Terjadi kesalahan saat prediksi: {e}"}
            print(f"Error saat memanggil predict_new_data: {e}")

    return render_template('index.html', result=result, available_models=available_models)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)