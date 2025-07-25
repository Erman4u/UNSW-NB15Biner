Deteksi Anomali Jaringan dengan Berbagai Model Machine Learning
! (https://placehold.co/800x400/aabbcc/ffffff?text=Deteksi+Anomali+Jaringan)

Proyek ini adalah aplikasi web sederhana berbasis Flask untuk mendeteksi anomali (serangan) pada trafik jaringan menggunakan beberapa model Machine Learning yang berbeda. Pengguna dapat memasukkan parameter trafik jaringan dan memilih model klasifikasi yang ingin digunakan untuk prediksi.

Fitur Utama
Pilihan Model: Pengguna dapat memilih antara berbagai model Machine Learning untuk prediksi, termasuk:

Logistic Regression

Random Forest

Support Vector Machine (SVM)

Naive Bayes

K-Nearest Neighbors (KNN)

Prediksi Real-time: Dapatkan hasil prediksi (Normal atau Anomali) dan probabilitas terkait secara instan.

Probabilitas Ganda: Menampilkan probabilitas untuk kelas "Anomali" dan "Normal" untuk pemahaman yang lebih baik tentang keyakinan model.

Isi Data Otomatis: Tombol praktis untuk mengisi formulir dengan contoh data trafik "Normal" atau "Anomali" untuk pengujian cepat.

Antarmuka Pengguna Sederhana: Antarmuka berbasis web yang intuitif untuk memasukkan data trafik.

Model yang Digunakan
Proyek ini menggunakan model-model klasifikasi berikut yang telah dilatih pada dataset deteksi anomali jaringan:

Logistic Regression: Model linier untuk klasifikasi.

Random Forest: Ensemble dari decision tree yang kuat, baik untuk data kompleks.

Support Vector Machine (SVM): Model yang mencari hyperplane optimal untuk memisahkan kelas.

Naive Bayes (GaussianNB): Model probabilistik berdasarkan Teorema Bayes.

K-Nearest Neighbors (KNN): Model berbasis instansi yang mengklasifikasikan data berdasarkan tetangga terdekat.

Semua model dan preprocessor (seperti LabelEncoder dan StandardScaler) disimpan dalam format .pkl di direktori model/.

Persyaratan Sistem
Python 3.x

pip (manajer paket Python)

Instalasi dan Setup
Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di lingkungan lokal Anda:

Kloning Repositori:
Buka Command Prompt (CMD) atau terminal Anda dan kloning repositori ini:

git clone https://github.com/NamaPenggunaAnda/Deteksi-Anomali-Jaringan.git
cd Deteksi-Anomali-Jaringan

(Ganti NamaPenggunaAnda/Deteksi-Anomali-Jaringan.git dengan URL repositori Anda yang sebenarnya.)

Buat dan Aktifkan Virtual Environment:
Sangat disarankan untuk menggunakan virtual environment untuk mengelola dependencies.

python -m venv venv

Untuk Windows:

venv\Scripts\activate

Untuk macOS/Linux:

source venv/bin/activate

Instal Dependencies:
Setelah virtual environment aktif, instal semua library yang diperlukan:

pip install Flask joblib pandas scikit-learn

Siapkan Model (Penting!):
Pastikan Anda telah melatih dan menyimpan semua model (logistic_regression_model.pkl, random_forest_model.pkl, svm_model.pkl, naive_bayes_model.pkl, knn_model.pkl) serta preprocessor (encoder_flag.pkl, encoder_protocol_type.pkl, encoder_service.pkl, scaler.pkl) di dalam folder model/ di direktori proyek Anda. Jika Anda tidak memiliki model-model ini, aplikasi tidak akan berjalan.

Menjalankan Aplikasi
Setelah semua dependencies terinstal dan virtual environment aktif, Anda dapat menjalankan aplikasi Flask:

python app.py

Anda akan melihat output di terminal yang menunjukkan bahwa aplikasi sedang berjalan. Cari baris seperti:

 * Running on http://127.0.0.1:5000

Mengakses Aplikasi
Buka browser web Anda dan kunjungi alamat yang tertera di terminal (biasanya http://127.0.0.1:5000/ atau http://localhost:5000/).

Cara Menggunakan Aplikasi
Pilih Model: Gunakan dropdown "Pilih Model" untuk memilih salah satu model klasifikasi yang tersedia.

Isi Data Trafik:

Anda dapat mengisi setiap kolom input secara manual dengan nilai-nilai trafik jaringan.

Atau, gunakan tombol "Isi Data Normal" atau "Isi Data Anomali" untuk mengisi formulir secara otomatis dengan contoh data.

Lakukan Prediksi: Klik tombol "Prediksi".

Lihat Hasil: Hasil prediksi (Status: ANOMALI/NORMAL) dan probabilitas untuk Anomali dan Normal akan ditampilkan di bawah formulir.

Catatan Penting
Mode Debug: Aplikasi berjalan dalam mode debug (debug=True) untuk pengembangan. Jangan gunakan mode ini untuk deployment produksi.

Versi Scikit-learn: Anda mungkin melihat peringatan InconsistentVersionWarning jika versi scikit-learn saat model dilatih berbeda dengan versi yang terinstal. Untuk mengatasi ini, disarankan untuk melatih ulang model Anda dengan versi scikit-learn yang sama dengan yang Anda gunakan untuk deployment, atau sesuaikan versi scikit-learn di virtual environment Anda.

Selamat menggunakan aplikasi Deteksi Anomali Jaringan ini!