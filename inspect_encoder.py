<<<<<<< HEAD
import joblib
import pickle
from sklearn.preprocessing import LabelEncoder # Penting jika file berisi LabelEncoder

# Tentukan path ke file .pkl Anda
# Pastikan Anda menjalankan skrip ini dari direktori yang sama dengan folder 'model'
# Atau sesuaikan path-nya agar benar.
# Contoh: 'model/encoders.pkl' jika skrip ini di folder NSL_Erman
pkl_file_path = 'model/encoders.pkl'

print(f"Mencoba memuat file: {pkl_file_path}")

try:
    # Coba muat menggunakan joblib (paling umum untuk model ML dan encoder)
    loaded_object = joblib.load(pkl_file_path)
    print("\nBerhasil memuat file menggunakan joblib!")
    print(f"Tipe objek yang dimuat: {type(loaded_object)}")

    # Sekarang, kita bisa mencoba melihat isinya
    if isinstance(loaded_object, dict):
        print("\nObjek yang dimuat adalah DICTIONARY (kamus).")
        print("Kunci-kunci dalam kamus:")
        for key, value in loaded_object.items():
            print(f"- Kunci: '{key}', Tipe Nilai: {type(value)}")
            # Jika nilai adalah LabelEncoder, kita bisa melihat kelasnya
            if isinstance(value, LabelEncoder):
                print(f"  Kelas-kelas dalam LabelEncoder ini: {value.classes_}")
    elif isinstance(loaded_object, LabelEncoder):
        print("\nObjek yang dimuat adalah SATU LabelEncoder tunggal.")
        print(f"Kelas-kelas dalam LabelEncoder ini: {loaded_object.classes_}")
    else:
        print("\nObjek yang dimuat adalah tipe lain. Berikut representasi stringnya:")
        print(loaded_object)

except Exception as e:
    print(f"\nGagal memuat file menggunakan joblib. Mencoba dengan pickle.load(). Error: {e}")
    try:
        # Jika joblib gagal, coba dengan pickle standar
        with open(pkl_file_path, 'rb') as f:
            loaded_object = pickle.load(f)
        print("\nBerhasil memuat file menggunakan pickle.load()!")
        print(f"Tipe objek yang dimuat: {type(loaded_object)}")

        if isinstance(loaded_object, dict):
            print("\nObjek yang dimuat adalah DICTIONARY (kamus).")
            print("Kunci-kunci dalam kamus:")
            for key, value in loaded_object.items():
                print(f"- Kunci: '{key}', Tipe Nilai: {type(value)}")
                if isinstance(value, LabelEncoder):
                    print(f"  Kelas-kelas dalam LabelEncoder ini: {value.classes_}")
        elif isinstance(loaded_object, LabelEncoder):
            print("\nObjek yang dimuat adalah SATU LabelEncoder tunggal.")
            print(f"Kelas-kelas dalam LabelEncoder ini: {loaded_object.classes_}")
        else:
            print("\nObjek yang dimuat adalah tipe lain. Berikut representasi stringnya:")
            print(loaded_object)

    except Exception as e_pickle:
        print(f"\nJuga gagal memuat file menggunakan pickle.load(). Error: {e_pickle}")
        print("File .pkl mungkin rusak atau dibuat dengan versi library yang sangat berbeda.")

=======
import joblib
import pickle
from sklearn.preprocessing import LabelEncoder # Penting jika file berisi LabelEncoder

# Tentukan path ke file .pkl Anda
# Pastikan Anda menjalankan skrip ini dari direktori yang sama dengan folder 'model'
# Atau sesuaikan path-nya agar benar.
# Contoh: 'model/encoders.pkl' jika skrip ini di folder NSL_Erman
pkl_file_path = 'model/encoders.pkl'

print(f"Mencoba memuat file: {pkl_file_path}")

try:
    # Coba muat menggunakan joblib (paling umum untuk model ML dan encoder)
    loaded_object = joblib.load(pkl_file_path)
    print("\nBerhasil memuat file menggunakan joblib!")
    print(f"Tipe objek yang dimuat: {type(loaded_object)}")

    # Sekarang, kita bisa mencoba melihat isinya
    if isinstance(loaded_object, dict):
        print("\nObjek yang dimuat adalah DICTIONARY (kamus).")
        print("Kunci-kunci dalam kamus:")
        for key, value in loaded_object.items():
            print(f"- Kunci: '{key}', Tipe Nilai: {type(value)}")
            # Jika nilai adalah LabelEncoder, kita bisa melihat kelasnya
            if isinstance(value, LabelEncoder):
                print(f"  Kelas-kelas dalam LabelEncoder ini: {value.classes_}")
    elif isinstance(loaded_object, LabelEncoder):
        print("\nObjek yang dimuat adalah SATU LabelEncoder tunggal.")
        print(f"Kelas-kelas dalam LabelEncoder ini: {loaded_object.classes_}")
    else:
        print("\nObjek yang dimuat adalah tipe lain. Berikut representasi stringnya:")
        print(loaded_object)

except Exception as e:
    print(f"\nGagal memuat file menggunakan joblib. Mencoba dengan pickle.load(). Error: {e}")
    try:
        # Jika joblib gagal, coba dengan pickle standar
        with open(pkl_file_path, 'rb') as f:
            loaded_object = pickle.load(f)
        print("\nBerhasil memuat file menggunakan pickle.load()!")
        print(f"Tipe objek yang dimuat: {type(loaded_object)}")

        if isinstance(loaded_object, dict):
            print("\nObjek yang dimuat adalah DICTIONARY (kamus).")
            print("Kunci-kunci dalam kamus:")
            for key, value in loaded_object.items():
                print(f"- Kunci: '{key}', Tipe Nilai: {type(value)}")
                if isinstance(value, LabelEncoder):
                    print(f"  Kelas-kelas dalam LabelEncoder ini: {value.classes_}")
        elif isinstance(loaded_object, LabelEncoder):
            print("\nObjek yang dimuat adalah SATU LabelEncoder tunggal.")
            print(f"Kelas-kelas dalam LabelEncoder ini: {loaded_object.classes_}")
        else:
            print("\nObjek yang dimuat adalah tipe lain. Berikut representasi stringnya:")
            print(loaded_object)

    except Exception as e_pickle:
        print(f"\nJuga gagal memuat file menggunakan pickle.load(). Error: {e_pickle}")
        print("File .pkl mungkin rusak atau dibuat dengan versi library yang sangat berbeda.")

>>>>>>> a6814b0ad77fa04c2431724eea35d697e7b60b56
print("\n--- Selesai ---")