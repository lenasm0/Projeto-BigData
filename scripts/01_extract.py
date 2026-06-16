import pandas as pd
import os

os.makedirs("data/raw/separated", exist_ok=True)

arquivo = "data/raw/gaming-vs-academic-performance/Gaming_Academic_Performance.csv"

df = pd.read_csv(arquivo)

# Dados Acadêmicos
academic = df[
    ["student_id", "study_hours", "attendance", "grades"]
]

academic.to_csv(
    "data/raw/separated/academic.csv",
    index=False
)

# Dados de Jogos
gaming = df[
    ["student_id", "gaming_hours", "gaming_genre"]
]

gaming.to_csv(
    "data/raw/separated/gaming.csv",
    index=False
)

# Dados Pessoais
personal = df[
    [
        "student_id",
        "age",
        "gender",
        "stress_level",
        "social_activity"
    ]
]

personal.to_csv(
    "data/raw/separated/personal.csv",
    index=False
)

# Dados de Saúde
health = df[
    [
        "student_id",
        "sleep_hours",
        "addiction_score"
    ]
]

health.to_csv(
    "data/raw/separated/health.csv",
    index=False
)

print("CSVs gerados com sucesso!")