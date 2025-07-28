Deteksi Anomali Jaringan dengan Berbagai Model Machine Learning
Proyek ini menghadirkan aplikasi web sederhana berbasis Flask yang dirancang untuk mendeteksi anomali (serangan) pada trafik jaringan. Aplikasi ini memanfaatkan beragam model Machine Learning untuk memberikan prediksi yang cepat dan informatif. Pengguna dapat memasukkan parameter trafik jaringan secara manual atau menggunakan contoh data, lalu memilih model klasifikasi yang ingin digunakan untuk proses deteksi.

Fitur Utama
Pilihan Model Prediksi: Anda dapat memilih salah satu dari berbagai model Machine Learning yang tersedia untuk melakukan prediksi, termasuk:

Logistic Regression

Random Forest

Support Vector Machine (SVM)

Naive Bayes (GaussianNB)

K-Nearest Neighbors (KNN)

Prediksi Real-time: Dapatkan hasil prediksi (Normal atau Anomali) secara instan setelah data dimasukkan.

Probabilitas Ganda: Hasil prediksi tidak hanya menunjukkan status (Normal/Anomali), tetapi juga menampilkan probabilitas untuk kedua kelas, memberikan pemahaman yang lebih dalam tentang keyakinan model.

Isi Data Otomatis: Tersedia tombol praktis untuk mengisi formulir secara otomatis dengan contoh data trafik Normal atau Anomali, mempermudah pengujian cepat.

Antarmuka Pengguna Sederhana: Antarmuka web yang intuitif dan mudah digunakan untuk memasukkan parameter trafik jaringan.

Model dan Preprocessor yang Digunakan
Proyek ini memanfaatkan model-model klasifikasi berikut yang telah dilatih pada dataset deteksi anomali jaringan, kemungkinan besar adalah dataset UNSW-NB15 atau yang serupa:

Logistic Regression: Model linear sederhana namun efektif untuk klasifikasi biner.

Random Forest: Model ensemble berbasis pohon keputusan yang kuat, cocok untuk menangani data kompleks dan memberikan akurasi tinggi.

Support Vector Machine (SVM): Model yang mencari hyperplane optimal untuk memisahkan kelas dengan margin terbesar.

Naive Bayes (GaussianNB): Model probabilistik yang didasarkan pada Teorema Bayes, cocok untuk dataset besar dan memiliki kinerja yang cepat.

K-Nearest Neighbors (KNN): Model berbasis instansi yang mengklasifikasikan data baru berdasarkan mayoritas kelas dari tetangga terdekatnya.

Semua model yang telah dilatih, serta preprocessor (seperti LabelEncoder untuk fitur kategorikal dan StandardScaler untuk fitur numerik), disimpan dalam format .pkl di direktori model/ proyek ini.

Persyaratan Sistem
Pastikan sistem Anda memenuhi persyaratan berikut:

Python 3.x

pip (manajer paket Python)

Instalasi dan Setup
Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di lingkungan lokal Anda:

Kloning Repositori:
Buka Command Prompt (CMD) atau terminal Anda dan kloning repositori ini:

Bash

git clone https://github.com/NamaPenggunaAnda/Deteksi-Anomali-Jaringan.git
cd Deteksi-Anomali-Jaringan
(Ganti NamaPenggunaAnda/Deteksi-Anomali-Jaringan.git dengan URL repositori Anda yang sebenarnya.)

Buat dan Aktifkan Virtual Environment:
Sangat disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek secara terisolasi.

Bash

python -m venv venv
Untuk Windows:

Bash

venv\Scripts\activate
Untuk macOS/Linux:

Bash

source venv/bin/activate
Instal Dependensi:
Setelah virtual environment aktif, instal semua library Python yang diperlukan:

Bash

pip install Flask joblib pandas scikit-learn
Siapkan Model dan Preprocessor (Penting!):
Pastikan Anda telah melatih dan menyimpan semua file model (logistic_regression_model.pkl, random_forest_model.pkl, svm_model.pkl, naive_bayes_model.pkl, knn_model.pkl) serta preprocessor (encoder_flag.pkl, encoder_protocol_type.pkl, encoder_service.pkl, scaler.pkl) di dalam folder model/ di direktori proyek Anda.

Catatan: Aplikasi tidak akan berjalan jika file-file model atau preprocessor yang diperlukan tidak ditemukan. Anda dapat melatih model-model ini sendiri atau mendapatkannya dari sumber lain yang kompatibel.

Menjalankan Aplikasi
Setelah semua dependensi terinstal dan virtual environment aktif, Anda dapat menjalankan aplikasi Flask:

Bash

python app.py
Anda akan melihat output di terminal yang menunjukkan bahwa aplikasi sedang berjalan. Cari baris seperti:

* Running on http://127.0.0.1:5000
Mengakses Aplikasi
Buka browser web Anda dan kunjungi alamat yang tertera di terminal (biasanya http://127.0.0.1:5000/ atau http://localhost:5000/).

Cara Menggunakan Aplikasi
Pilih Model: Gunakan dropdown "Pilih Model" untuk memilih salah satu model klasifikasi yang tersedia.

Isi Data Trafik:

Anda dapat mengisi setiap kolom input secara manual dengan nilai-nilai trafik jaringan yang ingin Anda prediksi.

Atau, gunakan tombol "Isi Data Normal" atau "Isi Data Anomali" untuk mengisi formulir secara otomatis dengan contoh data yang telah disediakan.

Lakukan Prediksi: Klik tombol "Prediksi".

Lihat Hasil: Hasil prediksi (Status: ANOMALI / NORMAL) dan probabilitas untuk Anomali dan Normal akan ditampilkan di bawah formulir.

Catatan Penting
Mode Debug: Aplikasi berjalan dalam mode debug (debug=True) untuk tujuan pengembangan. JANGAN gunakan mode ini untuk deployment produksi karena dapat menimbulkan risiko keamanan.

Versi Scikit-learn: Anda mungkin melihat peringatan InconsistentVersionWarning jika versi scikit-learn saat model dilatih berbeda dengan versi yang terinstal di lingkungan Anda. Untuk mengatasi ini, disarankan untuk melatih ulang model Anda dengan versi scikit-learn yang sama dengan yang Anda gunakan untuk deployment, atau sesuaikan versi scikit-learn di virtual environment Anda.
