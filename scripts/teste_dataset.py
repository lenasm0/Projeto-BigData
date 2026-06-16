import pandas as pd

arquivo = r"data/raw/gaming-vs-academic-performance/Gaming_Academic_Performance.csv"

df = pd.read_csv(arquivo)

print(df.head())

print("\nCOLUNAS:")
print(df.columns.tolist())