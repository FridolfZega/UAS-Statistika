import pandas as pd

# 1. Baca file CSV asli
file_path = "Student_performance_data _.csv"  # Ganti sesuai nama file jika berbeda
df = pd.read_csv(file_path)

# 2. Ambil hanya kolom yang relevan
selected_columns = ['StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport', 'GPA']
df_clean = df[selected_columns].copy()

# 3. Hapus duplikasi
df_clean = df_clean.drop_duplicates()

# 4. Hapus nilai kosong
df_clean = df_clean.dropna()

# 5. Validasi rentang nilai
df_clean = df_clean[
    (df_clean['StudyTimeWeekly'] >= 0) & (df_clean['StudyTimeWeekly'] <= 80) &
    (df_clean['Absences'] >= 0) &
    (df_clean['Tutoring'].isin([0, 1])) &
    (df_clean['ParentalSupport'].between(1, 4)) &  # Asumsi skala dukungan orang tua 1–4
    (df_clean['GPA'] >= 0) & (df_clean['GPA'] <= 4)
]

# 6. Simpan hasil ke file baru (opsional)
df_clean.to_csv("Cleaned_Selected_Variables.csv", index=False)

# 7. Tampilkan hasil awal
print("Data setelah dibersihkan (variabel terpilih):")
print(df_clean.head())
