import pandas as pd
from scipy import stats

# 1. Baca file hasil cleaning
file_path = "Cleaned_Selected_Variables.csv"
df = pd.read_csv(file_path)

# 2. Ambil semua kolom yang ada dalam file
columns = df.columns

# 3. Hitung dan tampilkan statistik deskriptif
for col in columns:
    print(f"\n--- Statistik untuk {col} ---")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    if not df[col].mode().empty:
        print("Mode:", df[col].mode().iloc[0])
    else:
        print("Mode: Tidak ada")
    print("Standard Deviation:", df[col].std())
    print("Range:", df[col].max() - df[col].min())
    print("Q1 (25%):", df[col].quantile(0.25))
    print("Q2 (Median):", df[col].quantile(0.50))
    print("Q3 (75%):", df[col].quantile(0.75))
