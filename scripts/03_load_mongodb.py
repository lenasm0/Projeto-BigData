import pandas as pd
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["academic_gaming"]

colecoes = {
    "academic": "academic_clean.parquet",
    "gaming": "gaming_clean.parquet",
    "personal": "personal_clean.parquet",
    "health": "health_clean.parquet"
}

for colecao, arquivo in colecoes.items():

    df = pd.read_parquet(
        f"data/processed/{arquivo}"
    )

    registros = df.to_dict(
        orient="records"
    )

    if registros:
        db[colecao].insert_many(
            registros
        )

    print(
        f"{colecao} carregada"
    )

print("Carga finalizada")