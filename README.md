# Projeto Big Data - Análise da Relação entre Jogos e Desempenho Acadêmico

## Objetivo

Este projeto implementa um pipeline de ingestão de Big Data utilizando dados sobre hábitos de jogos eletrônicos e desempenho acadêmico de estudantes.

O objetivo é capturar, transformar, armazenar e analisar os dados para identificar padrões comportamentais relacionados ao desempenho escolar.

---

## Dataset Utilizado

Fonte:

https://www.kaggle.com/datasets/aiexplorer77/gaming-vs-academic-performance

O dataset contém informações sobre:

* Horas de estudo
* Horas jogando
* Frequência escolar
* Notas
* Horas de sono
* Nível de estresse
* Perfil dos estudantes

---

## Arquitetura da Solução

Kaggle
↓
CSV
↓
Separação dos Dados
↓
Limpeza e Validação
↓
Conversão para Parquet
↓
MongoDB
↓
Análises

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* PyArrow
* MongoDB
* MongoDB Compass

---

## Estrutura do Projeto

games-academic-bigdata

├── data

│   ├── raw

│   ├── separated

│   └── processed

│

├── scripts

│   ├── 01_extract.py

│   ├── 02_transform.py

│   ├── 03_load_mongodb.py

│   └── 04_analysis.py

│

├── requirements.txt

└── README.md

---

## Etapas do Pipeline

### 1. Extração

Leitura do dataset original disponibilizado no Kaggle.

Script:

scripts/01_extract.py

Responsável por separar os dados em:

* academic.csv
* gaming.csv
* personal.csv
* health.csv

---

### 2. Transformação

Script:

scripts/02_transform.py

Operações realizadas:

* Remoção de registros duplicados
* Tratamento de valores nulos
* Padronização de categorias
* Conversão para formato Parquet

Arquivos gerados:

* academic_clean.parquet
* gaming_clean.parquet
* personal_clean.parquet
* health_clean.parquet

---

### 3. Carga

Script:

scripts/03_load_mongodb.py

Responsável por carregar os arquivos Parquet para o MongoDB.

Coleções criadas:

* academic
* gaming
* personal
* health

---

### 4. Análises

Script:

scripts/04_analysis.py

Análises realizadas:

* Relação entre horas jogando e notas
* Impacto do sono no desempenho acadêmico
* Influência das horas de estudo
* Impacto do estresse
* Perfil dos estudantes
* Identificação de risco de baixa performance

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

---

## MongoDB

Abrir o Mongo Shell:

mongosh

Selecionar banco:

use academic_gaming

Listar coleções:

show collections

---

## Resultados Esperados

O sistema deverá:

* Separar os dados em múltiplos domínios
* Realizar limpeza e padronização
* Converter os dados para Parquet
* Carregar os dados no MongoDB
* Gerar análises estatísticas sobre desempenho acadêmico e hábitos de jogos

---

## Autor(es)

Adicionar nome(s) dos integrantes do grupo.
