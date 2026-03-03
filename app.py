# import library
import streamlit as st
import pandas as pd
import joblib

# Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Keputusan Mahasiswa", page_icon="🎓", layout="centered")

# 1. Load Model dan Scaler
@st.cache_resource
def load_models():
    model = joblib.load('model/rf_model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    le = joblib.load('model/label_encoder.pkl')
    return model, scaler, le

try:
    model, scaler, le = load_models()
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan")

# 2. Header Aplikasi
st.title("🎓 Jaya Jaya Institut")
st.title("Early Warning System")
st.write("""
Aplikasi ini dirancang untuk mendeteksi dini apakah seorang mahasiswa berisiko **Dropout**, 
akan tetap **Enrolled**, atau berhasil **Graduate** menggunakan model Machine Learning *Random Forest*.
""")
st.markdown("---")

# 3. Sidebar Khusus Untuk Mode Navigasi
st.sidebar.header("⚙️ Mode Aplikasi")
app_mode = st.sidebar.radio("Pilih Metode Prediksi:", ["Prediksi Manual", "Prediksi via Upload CSV"])

# MODE 1: PREDIKSI MANUAL
if app_mode == "Prediksi Manual":
    st.subheader("📋 Form Prediksi Mahasiswa")
    
    # Membagi layar jadi 2 kolom (Kiri dan Kanan)
    col1, col2 = st.columns(2)
    
    # KIRI: 4 Input (Finansial & Demografi)
    with col1:
        st.markdown("**Faktor Finansial & Demografi**")
        tuition_fees = st.selectbox("Status SPP (Tuition Fees)", [1, 0], format_func=lambda x: "Lunas (1)" if x == 1 else "Menunggak (0)")
        debtor = st.selectbox("Punya Hutang (Debtor)", [0, 1], format_func=lambda x: "Tidak (0)" if x == 0 else "Ya (1)")
        scholarship = st.selectbox("Penerima Beasiswa", [0, 1], format_func=lambda x: "Tidak (0)" if x == 0 else "Ya (1)")
        gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Perempuan (0)" if x == 0 else "Laki-laki (1)")

    # KANAN: 3 Input (Akademik & Umur) + 1 Tombol
    with col2:
        st.markdown("**Faktor Akademik & Umur**")
        age = st.number_input("Umur Saat Mendaftar", min_value=15, max_value=80, value=20)
        sem1_grade = st.number_input("Rata-rata Nilai Semester 1 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
        sem2_grade = st.number_input("Rata-rata Nilai Semester 2 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
        
        # Spacer agar tombol sejajar dengan form input baris ke-4
        st.write("") 
        predict_btn = st.button("🔍 Prediksi Sekarang", use_container_width=True)

    # FITUR LAINNYA DI EXPANDER (Tersembunyi)
    with st.expander("⚙️ Faktor Lainnya (Nilai Default)"):
        st.info("Variabel di bawah ini diisi dengan nilai rata-rata dari dataset untuk mempermudah simulasi. Anda dapat mengubahnya jika perlu.")
        col3, col4 = st.columns(2)
        with col3:
            sem1_approved = st.number_input("SKS Lulus Semester 1", min_value=0, max_value=20, value=5)
            marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6], index=0)
            unemployment_rate = st.number_input("Tingkat Pengangguran (%)", value=11.6)
        with col4:
            sem2_approved = st.number_input("SKS Lulus Semester 2", min_value=0, max_value=20, value=5)
            admission_grade = st.number_input("Nilai Ujian Masuk (0-200)", min_value=0.0, max_value=200.0, value=127.0)
            inflation_rate = st.number_input("Tingkat Inflasi (%)", value=1.2)
            gdp = st.number_input("GDP", value=1.7)

    # EKSEKUSI TOMBOL PREDIKSI MANUAL
    if predict_btn:
        # Nilai awal (untuk input data 36 kolom, hasil dari rata rata data sesuai training)
        input_data = {
            'Marital_status': marital_status, 'Application_mode': 1, 'Application_order': 1, 'Course': 9085, 
            'Daytime_evening_attendance': 1, 'Previous_qualification': 1, 'Previous_qualification_grade': 132.0,
            'Nacionality': 1, 'Mothers_qualification': 19, 'Fathers_qualification': 19, 'Mothers_occupation': 5,
            'Fathers_occupation': 5, 'Admission_grade': admission_grade, 'Displaced': 1, 'Educational_special_needs': 0,
            'Debtor': debtor, 'Tuition_fees_up_to_date': tuition_fees, 'Gender': gender, 'Scholarship_holder': scholarship,
            'Age_at_enrollment': age, 'International': 0, 'Curricular_units_1st_sem_credited': 0,
            'Curricular_units_1st_sem_enrolled': 6, 'Curricular_units_1st_sem_evaluations': 8,
            'Curricular_units_1st_sem_approved': sem1_approved, 'Curricular_units_1st_sem_grade': sem1_grade,
            'Curricular_units_1st_sem_without_evaluations': 0, 'Curricular_units_2nd_sem_credited': 0,
            'Curricular_units_2nd_sem_enrolled': 6, 'Curricular_units_2nd_sem_evaluations': 8,
            'Curricular_units_2nd_sem_approved': sem2_approved, 'Curricular_units_2nd_sem_grade': sem2_grade,
            'Curricular_units_2nd_sem_without_evaluations': 0, 'Unemployment_rate': unemployment_rate,
            'Inflation_rate': inflation_rate, 'GDP': gdp
        }

        df_input = pd.DataFrame([input_data])
        scaled_input = scaler.transform(df_input)
        prediction = model.predict(scaled_input)[0]
        predicted_status = le.inverse_transform([prediction])[0]
        
        # Hasil prediksi
        st.markdown("---")
        st.subheader("💡 Hasil Analisis Sistem:")
        
        if predicted_status == 'Dropout':
            st.error(f"⚠️ **Peringatan Tinggi:** Mahasiswa ini diprediksi akan **{predicted_status}**!")
            st.write("Rekomendasi: Segera panggil mahasiswa untuk sesi konseling akademik atau tawarkan program relaksasi SPP/Beasiswa.")
        elif predicted_status == 'Enrolled':
            st.warning(f"⏳ **Status Menengah:** Mahasiswa ini diprediksi tetap **{predicted_status}** (Belum Lulus/Menunda).")
            st.write("Rekomendasi: Pantau perkembangan nilai semester berikutnya dan berikan bimbingan skripsi/tugas akhir.")
        else:
            st.success(f"🎓 **Aman:** Mahasiswa ini diprediksi akan **{predicted_status}** (Lulus).")
            st.write("Rekomendasi: Pertahankan performa akademik mahasiswa. Tidak memerlukan intervensi khusus.")

# MODE 2: PREDIKSI UPLOAD CSV
elif app_mode == "Prediksi via Upload CSV":
    st.subheader("📁 Prediksi Massal via CSV")
    st.info("Unggah file CSV yang berisi data mahasiswa lengkap. Pastikan format kolom sama persis dengan dataset asli (tanpa kolom target 'Status').")
    
    uploaded_file = st.file_uploader("Upload File CSV Anda di sini:", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Membaca data CSV
            df_upload = pd.read_csv(uploaded_file, sep=None, engine='python')
            
            st.markdown("**Preview 5 Data Teratas:**")
            st.dataframe(df_upload.head(5))
            
            # Tombol Prediksi Massal
            if st.button("🚀 Prediksi Seluruh Data", use_container_width=True):
                # Melakukan scaling
                scaled_upload = scaler.transform(df_upload)
                
                # Memprediksi status
                predictions = model.predict(scaled_upload)
                
                # Mengubah angka tebakan menjadi teks
                status_labels = le.inverse_transform(predictions)
                
                # Menambahkan hasil prediksi ke tabel
                df_upload['Prediksi_Status'] = status_labels
                
                st.markdown("---")
                st.success("✅ Prediksi Selesai! Berikut adalah hasilnya:")
                
                # Menampilkan semua data hasil prediksi
                st.dataframe(df_upload)
                
                # Fitur Download CSV Hasil
                csv_hasil = df_upload.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="⬇️ Download Hasil Prediksi (CSV)",
                    data=csv_hasil,
                    file_name="hasil_prediksi_mahasiswa.csv",
                    mime="text/csv",
                )
        except ValueError as ve:
            st.error(f"Gagal memproses. Pastikan file CSV memiliki 36 kolom fitur yang tepat. Error: {ve}")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")