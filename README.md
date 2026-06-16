# Projeto Big Data - Análise de Jogos e Desempenho Acadêmico

## Objetivo

Implementar um pipeline de ingestão de Big Data utilizando MongoDB para analisar a relação entre hábitos de jogos eletrônicos e desempenho acadêmico dos estudantes.

O projeto contempla as etapas de extração, transformação, armazenamento e análise dos dados.

---

## Dataset

Fonte dos dados:

https://www.kaggle.com/datasets/aiexplorer77/gaming-vs-academic-performance

Informações disponíveis:

* Horas jogando
* Horas estudando
* Horas de sono
* Frequência escolar
* Nível de estresse
* Gênero
* Notas acadêmicas
* Score de dependência em jogos

---

## Arquitetura da Solução

Kaggle

↓

Dataset CSV

↓

Separação dos Dados

↓

Limpeza e Transformação

↓

Arquivos Parquet

↓

MongoDB

↓

Dashboard Analítico

---

## Tecnologias Utilizadas

* Python
* Pandas
* PyArrow
* MongoDB
* MongoDB Compass
* Streamlit
* Matplotlib
* Git
* GitHub

---

## Estrutura do Projeto

games-academic-bigdata

├── data

│ ├── raw

│ ├── separated

│ └── processed

│

├── scripts

│ ├── 01_extract.py

│ ├── 02_transform.py

│ ├── 03_load_mongodb.py

│ ├── 04_analysis.py

│

├── dashboard.py

├── requirements.txt

├── README.md

---

## Etapa 1 - Extração

Arquivo:

scripts/01_extract.py

Responsável por:

* Ler o dataset original
* Separar os dados por domínio

Arquivos gerados:

* academic.csv
* gaming.csv
* personal.csv
* health.csv

---

## Etapa 2 - Transformação

Arquivo:

scripts/02_transform.py

Responsável por:

* Remover duplicidades
* Tratar valores nulos
* Padronizar dados
* Converter CSV para Parquet

Arquivos gerados:

* academic_clean.parquet
* gaming_clean.parquet
* personal_clean.parquet
* health_clean.parquet

---

## Etapa 3 - Carga no MongoDB

Arquivo:

scripts/03_load_mongodb.py

Responsável por:

* Ler os arquivos Parquet
* Inserir os dados no MongoDB

Coleções criadas:

* academic
* gaming
* personal
* health

---

## Etapa 4 - Análises

Arquivo:

scripts/04_analysis.py

Análises realizadas:

* Horas jogando x notas
* Horas de estudo x notas
* Sono x desempenho
* Estresse x desempenho
* Segmentação dos estudantes

---

## Dashboard Analítico

Arquivo:

dashboard.py

O dashboard foi desenvolvido utilizando Streamlit para permitir visualização interativa dos resultados.

Funcionalidades:

* Indicadores gerais
* Filtros por gênero
* Filtros por nível de estresse
* Horas jogando x nota média
* Horas estudando x nota média
* Sono x nota média
* Distribuição do estresse
* Insights automáticos
* Visualização do dataset

---

## Como Executar

### Instalar dependências

pip install -r requirements.txt

### Executar extração

python scripts/01_extract.py

### Executar transformação

python scripts/02_transform.py

### Executar carga

python scripts/03_load_mongodb.py

### Executar análises

python scripts/04_analysis.py

### Executar dashboard

streamlit run dashboard.py

---

## MongoDB

Abrir Mongo Shell:

mongosh

Selecionar banco:

use academic_gaming

Listar coleções:

show collections

---

## Resultados Esperados

O projeto deve:

* Extrair dados do Kaggle
* Separar os dados por domínio
* Transformar os dados
* Converter para Parquet
* Carregar no MongoDB
* Realizar análises estatísticas
* Exibir dashboard interativo


