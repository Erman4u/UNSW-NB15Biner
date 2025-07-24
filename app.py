from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder # Tambahkan import ini

app = Flask(__name__)

# Load model dan encoder saat start
# model/rf_model.pkl adalah model klasifikasi Anda
# model/encoders.pkl sekarang kita tahu berisi SATU LabelEncoder untuk 'flag'
model = joblib.load('model/rf_model.pkl')
flag_encoder = joblib.load('model/encoders.pkl') # Ganti nama variabel menjadi flag_encoder

# Pastikan flag_encoder benar-benar objek LabelEncoder
if not isinstance(flag_encoder, LabelEncoder):
    raise TypeError("Objek yang dimuat dari 'encoders.pkl' bukan LabelEncoder yang diharapkan. "
                    "Periksa kembali file tersebut.")

# Manual mapping untuk protocol_type (karena tidak ada encoder di encoders.pkl)
# Ini adalah asumsi berdasarkan opsi di index.html
protocol_type_map = {
    'tcp': 0,
    'udp': 1,
    'icmp': 2
}

# Manual mapping untuk service (karena tidak ada encoder di encoders.pkl)
# Ini adalah asumsi berdasarkan opsi di index.html.
# Idealnya, ini harus sesuai dengan encoding yang digunakan saat model dilatih.
service_options = [
    "whois", "uucp_path", "uuurp", "urp_i", "urh_i", "time", "tim_i", "tftp_u",
    "telnet", "systat", "supdup", "sunrpc", "ssh", "sql_net", "smtp", "smtpi",
    "shell", "remote_job", "red_i", "private", "print_srv", "pop_3", "pop_2",
    "pm_udp", "other", "ntp_u", "netstat", "netbios_ns", "netbios_dgm",
    "netbios_ssn", "netmbe", "mtp", "login", "link", "ldap", "klogin", "kshell",
    "iso_tsap", "IRC", "http_8001", "http_443", "http_2784", "http", "hostname",
    "hostnames", "gopher", "ftp_data", "ftp", "finger", "exec", "efs", "eco_i",
    "echo", "domain_u", "domain", "discard", "daytime", "ctf", "csnet_ns",
    "courier", "bgp", "auth", "aol", "Z39_50", "X11"
]
service_map = {service: i for i, service in enumerate(service_options)}


# Daftar fitur yang dibutuhkan oleh model
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

def predict_new_data(new_data):
    df = pd.DataFrame([new_data])

    # --- Encoding untuk kolom 'flag' ---
    if 'flag' in df.columns:
        df['flag'] = df['flag'].apply(lambda x: flag_encoder.transform([x])[0] if x in flag_encoder.classes_ else -1)
    else:
        print("Peringatan: Kolom 'flag' tidak ditemukan di data input. Tidak dapat menerapkan flag_encoder.")
        # Jika kolom flag tidak ada, isi dengan nilai default numerik (misal 0)
        df['flag'] = 0

    # --- Encoding untuk 'protocol_type' ---
    if 'protocol_type' in df.columns:
        df['protocol_type'] = df['protocol_type'].apply(lambda x: protocol_type_map.get(x, -1)) # -1 for unknown
    else:
        print("Peringatan: Kolom 'protocol_type' tidak ditemukan di data input. Mengisi dengan 0.")
        df['protocol_type'] = 0

    # --- Encoding untuk 'service' ---
    if 'service' in df.columns:
        df['service'] = df['service'].apply(lambda x: service_map.get(x, -1)) # -1 for unknown
    else:
        print("Peringatan: Kolom 'service' tidak ditemukan di data input. Mengisi dengan 0.")
        df['service'] = 0

    # Pastikan semua fitur yang dibutuhkan ada, jika tidak, isi dengan 0
    # Ini penting untuk fitur numerik yang mungkin tidak diisi di form
    for col in REQUIRED_FEATURES:
        if col not in df.columns:
            df[col] = 0
        # Pastikan tipe data numerik sudah benar (setelah encoding kategorikal)
        # Jika ada kolom yang masih string karena suatu alasan, coba konversi ke numerik
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0) # Convert to numeric, fill NaN with 0
        except Exception as e:
            print(f"Peringatan: Gagal mengonversi kolom '{col}' ke numerik: {e}. Mengisi dengan 0.")
            df[col] = 0


    # Pastikan urutan kolom sesuai dengan yang dibutuhkan model
    df = df[REQUIRED_FEATURES]

    # Lakukan prediksi probabilitas
    proba = model.predict_proba(df)[0][1]
    pred = int(proba >= 0.4)

    return {'prediction': pred, 'probability': round(proba, 4)}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_data = {}
        for key in REQUIRED_FEATURES:
            # Ambil semua input sebagai string terlebih dahulu
            val = request.form.get(key)
            # Kemudian konversi ke float jika bukan kolom kategorikal
            if key in ['protocol_type', 'flag', 'service']:
                input_data[key] = val # Tetap string untuk encoding nanti
            else:
                try:
                    input_data[key] = float(val) if val else 0.0 # Konversi ke float, default 0.0 jika kosong
                except ValueError:
                    input_data[key] = 0.0 # Jika tidak bisa dikonversi, default 0.0

        try:
            result = predict_new_data(input_data)
        except Exception as e:
            result = {'prediction': -1, 'message': f"Terjadi kesalahan saat prediksi: {e}"}
            print(f"Error saat memanggil predict_new_data: {e}")

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
