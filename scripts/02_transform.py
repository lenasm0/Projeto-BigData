import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

arquivos = [
    "academic",
    "gaming",
    "personal",
    "health"
]

for nome in arquivos:

    caminho = f"data/raw/separated/{nome}.csv"

    df = pd.read_csv(caminho)

    # remover duplicados
    df = df.drop_duplicates()

    # tratar nulos
    df = df.fillna(0)

    # padronizar textos
    for col in df.select_dtypes(include="object"):
        df[col] = (
            df[col]
            .astype(str)
            .str.upper()
            .str.strip()
        )

    df.to_parquet(
        f"data/processed/{nome}_clean.parquet",
        index=False
    )

    print(f"{nome} convertido")