# Análise de Dados Públicos e Detecção de Anomalias com Isolation Forest

Este projeto apresenta um pipeline completo de **Engenharia de Dados** e **Machine Learning** focado na coleta, processamento e análise de dados públicos de notas fiscais para a **detecção de anomalias**. A metodologia central utiliza o algoritmo **Isolation Forest** para identificar padrões incomuns ou potencialmente fraudulentos em transações.

## 1. Visão Geral do Projeto

O objetivo principal é construir uma base de dados robusta a partir da API do Portal da Transparência e aplicar um modelo de *Machine Learning* não supervisionado para sinalizar transações que se desviam significativamente do comportamento normal.

### 1.1. Metodologia de Detecção de Anomalias

O projeto adota o **Isolation Forest** como principal ferramenta de detecção de anomalias.

> O Isolation Forest é um algoritmo baseado em árvores que isola anomalias (pontos raros e distintos) com muito mais facilidade do que os pontos normais. Ele mede a anomalia de uma observação pela profundidade média do caminho necessário para isolá-la em uma floresta de árvores aleatórias.

O modelo é aplicado no nível da nota fiscal, utilizando *features* enriquecidas (incluindo dados demográficos do IBGE e *features* temporais) para uma análise multidimensional.

## 2. Arquitetura e Estrutura do Código

A estrutura do projeto segue o padrão de organização de projetos de *Data Science* (DS), garantindo modularidade e clareza.

```
.
├── data/
│   ├── processed/              # Dados limpos e prontos para ML
│   ├── raw/                    # Dados brutos (ex: ibge_municipios.csv)
├── model/
│   ├── isolation_forest_model.joblib # Modelo treinado do Isolation Forest
│   ├── model_features.txt      # Lista de features usadas no treinamento
├── notebooks/
│   ├── 1_data_preprocessing.ipynb # Pré-processamento e Engenharia de Features
│   ├── 2_Isolation_forest.ipynb   # Treinamento e Avaliação do Modelo
├── src/
│   ├── config/                 # Configurações (API, Banco de Dados, Constantes)
│   ├── services/               # Lógica de Negócio (Coleta de API, Gerenciamento de DB)
│   ├── utils/                  # Funções Utilitárias (Limpeza de Dados, Conversão)
├── main.py                     # Ponto de entrada para orquestração da coleta
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

## 3. Tecnologias e Ferramentas

| Categoria | Ferramenta/Tecnologia | Função no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | Python | Linguagem principal para desenvolvimento e análise. |
| **Coleta de Dados** | `requests` | Requisições HTTP para a API do Portal da Transparência. |
| **Processamento** | `pandas`, `numpy` | Manipulação, limpeza e Engenharia de Features. |
| **Machine Learning** | `scikit-learn` | Implementação do algoritmo **Isolation Forest**. |
| **Persistência** | PostgreSQL, `psycopg2` | Banco de dados relacional para armazenamento dos dados coletados. |
| **Infraestrutura** | Servidor Linux Caseiro | Ambiente de execução e hospedagem do banco de dados. |

## 4. Fluxo de Execução (Pipeline)

O projeto é executado em três fases principais:

1.  **Coleta de Dados (main.py):**
    *   O script `main.py` orquestra a coleta de dados da API do Portal da Transparência.
    *   A coleta é realizada de forma **paralela** e **resiliente** (`src/services/api_collector.py`) para lidar com o grande volume de dados e a latência da rede.
    *   Os dados brutos são salvos diretamente no banco de dados PostgreSQL (`src/services/db_manager.py`).
2.  **Pré-processamento (1_data_preprocessing.ipynb):**
    *   Os dados são carregados do PostgreSQL.
    *   É realizada a limpeza de dados (`src/utils/data_cleaning.py`) e a conversão de formatos brasileiros (`src/utils/number_utils.py`).
    *   São criadas *features* avançadas (temporais, de razão, etc.) e o conjunto de dados é preparado para o modelo de ML.
3.  **Modelagem e Análise (2_Isolation_forest.ipynb):**
    *   O modelo **Isolation Forest** é treinado no conjunto de dados pré-processado.
    *   As notas fiscais são classificadas como **normais** ou **anômalas** com base no *score* de isolamento.
    *   O *notebook* inclui a avaliação do modelo com métricas adequadas para dados desbalanceados (ex: F1-Score, Precisão e Recall).

## 5. Configuração e Uso

Para configurar e executar o projeto, siga os passos abaixo:

### Pré-requisitos

*   Python 3.8+
*   PostgreSQL (configurado e acessível, conforme `src/config/database.py`)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd public-data-analysis-anomaly-detection-ml
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configuração:**
    *   Atualize as credenciais do PostgreSQL em `src/config/database.py`.
    *   Atualize a chave da API do Portal da Transparência em `src/config/api.py`.

### Execução da Coleta

Para iniciar a coleta de dados e salvá-los no PostgreSQL:

```bash
python main.py
```

### Análise e Modelagem

Para realizar o pré-processamento e treinar o modelo de ML, abra os *notebooks* Jupyter na ordem:

```bash
jupyter notebook notebooks/1_data_preprocessing.ipynb
jupyter notebook notebooks/2_Isolation_forest.ipynb
```

## 6. Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.
