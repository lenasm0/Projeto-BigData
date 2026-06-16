import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# configs

st.set_page_config(
    page_title="Gaming vs Academic Performance",
    page_icon="🎮",
    layout="wide"
)

# leitura

df = pd.read_csv(
    "data/raw/gaming-vs-academic-performance/Gaming_Academic_Performance.csv"
)

# titulo
st.title("Análise de Jogos e Desempenho Acadêmico")

st.markdown("""
Este dashboard apresenta análises sobre a relação entre hábitos de jogos,
estudo, sono e desempenho acadêmico dos estudantes.
""")

#filtros

st.sidebar.header("Filtros")

genero = st.sidebar.selectbox(
    "Gênero",
    ["Todos"] + sorted(df["gender"].unique().tolist())
)

estresse = st.sidebar.selectbox(
    "Nível de Estresse",
    ["Todos"] + sorted(df["stress_level"].unique().tolist())
)

if genero != "Todos":
    df = df[df["gender"] == genero]

if estresse != "Todos":
    df = df[df["stress_level"] == estresse]

# metricas gerais

st.subheader("Indicadores Gerais")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Estudantes",
    len(df)
)

c2.metric(
    "Nota Média",
    round(df["grades"].mean(), 2)
)

c3.metric(
    "Horas Jogando",
    round(df["gaming_hours"].mean(), 2)
)

c4.metric(
    "Horas Estudando",
    round(df["study_hours"].mean(), 2)
)

c5.metric(
    "Horas Sono",
    round(df["sleep_hours"].mean(), 2)
)

st.divider()

# jogar e notas

col1, col2 = st.columns(2)

with col1:

    st.subheader("Horas Jogando x Nota Média")

    temp = df.copy()

    temp["gaming_group"] = pd.cut(
        temp["gaming_hours"],
        bins=[0,2,4,6,8,10],
        labels=["0-2h","2-4h","4-6h","6-8h","8-10h"]
    )

    resultado = (
        temp.groupby("gaming_group")["grades"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(6,4))

    resultado.plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Nota Média")

    st.pyplot(fig)

# estudo e notas

with col2:

    st.subheader("Horas de Estudo x Nota Média")

    temp = df.copy()

    temp["study_group"] = pd.cut(
        temp["study_hours"],
        bins=[0,2,4,6,8,10],
        labels=["0-2h","2-4h","4-6h","6-8h","8-10h"]
    )

    resultado = (
        temp.groupby("study_group")["grades"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(6,4))

    resultado.plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Nota Média")

    st.pyplot(fig)

st.divider()

# sono e notas
col3, col4 = st.columns(2)

with col3:

    st.subheader("Sono x Nota Média")

    temp = df.copy()

    temp["sleep_group"] = pd.cut(
        temp["sleep_hours"],
        bins=[0,5,7,9,12],
        labels=["<5h","5-7h","7-9h",">9h"]
    )

    resultado = (
        temp.groupby("sleep_group")["grades"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(6,4))

    resultado.plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Nota Média")

    st.pyplot(fig)

# estresse

with col4:

    st.subheader("Distribuição do Estresse")

    estresse_count = (
        df["stress_level"]
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(6,4))

    estresse_count.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")

    st.pyplot(fig)

st.divider()

#dados finais

st.subheader("Principais Insights")

gaming_media = round(
    df["gaming_hours"].mean(),
    2
)

study_media = round(
    df["study_hours"].mean(),
    2
)

sono_media = round(
    df["sleep_hours"].mean(),
    2
)

nota_media = round(
    df["grades"].mean(),
    2
)

st.info(
    f"""
Nota média geral: {nota_media}

Média de horas jogando: {gaming_media}

Média de horas estudando: {study_media}

Média de horas de sono: {sono_media}

"""
)

# dado bruto

with st.expander("Visualizar Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )