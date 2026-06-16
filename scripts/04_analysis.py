import pandas as pd

df = pd.read_csv(
"data/raw/gaming-vs-academic-performance/Gaming_Academic_Performance.csv"
)

print("-"*60)
print("ANÁLISE 1 - HORAS JOGANDO X NOTAS")
print("-"*60)

df["gaming_group"] = pd.cut(
df["gaming_hours"],
bins=[0,2,4,6,8,10],
labels=[
"0-2h",
"2-4h",
"4-6h",
"6-8h",
"8-10h"
]
)

print(
df.groupby("gaming_group")["grades"]
.mean()
.round(2)
)

print("\n")

print("="*60)
print("ANÁLISE 2 - SONO X DESEMPENHO")
print("="*60)

df["sleep_group"] = pd.cut(
df["sleep_hours"],
bins=[0,5,7,9,12],
labels=[
"<5h",
"5-7h",
"7-9h",
">9h"
]
)

print(
df.groupby("sleep_group")["grades"]
.mean()
.round(2)
)

print("\n")

print("="*60)
print("ANÁLISE 3 - HORAS DE ESTUDO X NOTAS")
print("="*60)

df["study_group"] = pd.cut(
df["study_hours"],
bins=[0,2,4,6,8,10],
labels=[
"0-2h",
"2-4h",
"4-6h",
"6-8h",
"8-10h"
]
)

print(
df.groupby("study_group")["grades"]
.mean()
.round(2)
)

print("\n")

print("="*60)
print("ANÁLISE 4 - ESTRESSE X DESEMPENHO")
print("="*60)

print(
df.groupby("stress_level")["grades"]
.mean()
.round(2)
)

print("\n")

print("="*60)
print("ANÁLISE 5 - PERFIL DOS ESTUDANTES")
print("="*60)

print(
df.groupby("gender")
.agg({
"grades":"mean",
"gaming_hours":"mean",
"study_hours":"mean"
})
.round(2)
)

print("\n")

print("="*60)
print("ANÁLISE 6 - RISCO DE BAIXA PERFORMANCE")
print("="*60)

risco = df[
(df["grades"] < 60)
]

print(
"Quantidade de estudantes com nota abaixo de 60:"
)

print(
len(risco)
)

print("\nPercentual:")

print(
round(
len(risco) /
len(df) * 100,
2
),
"%"
)
