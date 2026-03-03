# System-Early-Warning-System-Prediksi-Keputusan-Mahasiswa
Aplikasi ini dirancang untuk mendeteksi dini apakah seorang mahasiswa berisiko Dropout,  akan tetap Enrolled, atau berhasil Graduate menggunakan model Machine Learning Random Forest.

# 🎓 Jaya Jaya Institut: Early Warning System (Student Attrition Prediction)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://system-early-warning-system-prediksi-keputusan-mahasiswa-aehxs.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Model-Random%20Forest-green.svg)](#)

Aplikasi berbasis web ini dirancang untuk mendeteksi dini risiko **Dropout** pada mahasiswa Jaya Jaya Institut. Dengan memanfaatkan model Machine Learning **Random Forest**, sistem ini dapat memprediksi apakah seorang mahasiswa berisiko *Dropout*, akan tetap *Enrolled* (Menunda/Belum Lulus), atau berhasil *Graduate* (Lulus) berdasarkan faktor akademik, finansial, dan demografi.

🔗 **Link Deployment (Live App):** [Jaya Jaya Institut - Early Warning System](https://system-early-warning-system-prediksi-keputusan-mahasiswa-aehxs.streamlit.app/)

---

## ✨ Fitur Utama
Aplikasi ini menyediakan 2 mode prediksi untuk menyesuaikan kebutuhan institusi:
1. **🔍 Prediksi 1 per 1 (Manual):** Evaluasi cepat menggunakan *form* interaktif. Pengguna cukup memasukkan 7 faktor risiko utama (seperti Status SPP, Usia, Nilai Semester, dan Beasiswa) untuk mendapatkan hasil seketika.
2. **📁 Prediksi Massal (Upload CSV):** Dirancang untuk evaluasi skala besar (ratusan/ribuan data sekaligus). Pengguna dapat mengunggah file CSV berisikan data mahasiswa, dan sistem akan memproses seluruh prediksi yang hasilnya dapat diunduh kembali dalam format CSV.

---

## 🛠️ Teknologi yang Digunakan
- **UI/Frontend:** Streamlit
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Model Serialization:** Joblib

---

## 📂 Struktur Repositori
```text
System-Early-Warning-System-Prediksi-Keputusan-Mahasiswa/
│
├── model/                     # Folder berisi model Machine Learning yang telah dilatih
│   ├── rf_model.pkl           # Model Random Forest
│   ├── scaler.pkl             # StandardScaler untuk normalisasi input
│   └── label_encoder.pkl      # LabelEncoder untuk konversi target
│
├── app.py                     # Script utama untuk menjalankan aplikasi Streamlit
├── requirements.txt           # Daftar library Python yang dibutuhkan
└── README.md                  # Dokumentasi repositori
```

## Cara Menjalankan Aplikasi di Komputer Lokal (Localhost)
### 1. Clone Repositori
Buka Terminal / Command Prompt dan jalankan perintah berikut:
```bash
git clone [https://github.com/rigger02/System-Early-Warning-System-Prediksi-Keputusan-Mahasiswa.git](https://github.com/rigger02/System-Early-Warning-System-Prediksi-Keputusan-Mahasiswa.git)
cd System-Early-Warning-System-Prediksi-Keputusan-Mahasiswa
```
### 2. Buat Virtual Environment (Opsional namun disarankan)
```bash
python -m venv env
# Untuk Windows:
env\Scripts\activate
# Untuk Mac/Linux:
source env/bin/activate
```
### 3. Install Dependencies
Pastikan semua library yang dibutuhkan terinstal dengan mengacu pada file requirements.txt:
```bash
pip install -r requirements.txt
```
### 4. Jalankan Aplikasi
Ketik perintah berikut untuk menjalankan server Streamlit:
```bash
streamlit run app.py
```
### 👤 Author
Rigger Damaiarta Tejayanda
Dicoding Profile: [rigger_dt]
Lulusan Teknik Informatika | Data Science Enthusiast
