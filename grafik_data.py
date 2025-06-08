import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = "Cleaned_Selected_Variables.csv"  # Ganti path jika file berada di lokasi berbeda
df = pd.read_csv(file_path)

# List of variables to visualize
columns = df.columns.tolist()

# Generate visualizations
for col in columns:
    plt.figure(figsize=(14, 10))

    # Histogram
    plt.subplot(2, 2, 1)
    plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Bar Chart (only if categorical or few unique values)
    plt.subplot(2, 2, 2)
    if df[col].nunique() < 10:
        df[col].value_counts().plot(kind='bar', color='lightcoral', edgecolor='black')
        plt.title(f'Bar Chart of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
    else:
        plt.text(0.5, 0.5, 'Not suitable for bar chart', ha='center', va='center')
        plt.axis('off')

    # Boxplot
    plt.subplot(2, 2, 3)
    sns.boxplot(x=df[col], color='lightgreen')
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)

    # Dot Plot
    plt.subplot(2, 2, 4)
    plt.plot(df[col], 'o', color='gray', alpha=0.6)
    plt.title(f'Dot Plot of {col}')
    plt.ylabel(col)
    plt.xlabel('Index')

    plt.tight_layout()
    plt.show()
