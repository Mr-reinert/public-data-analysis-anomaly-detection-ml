# Análise de Dados Públicos e Detecção de Anomalias com Machine Learning

Este projeto tem como objetivo coletar, processar e analisar dados públicos relacionados a notas fiscais, com foco na detecção de anomalias utilizando algoritmos de Machine Learning.  
A aplicação integra coleta automática de dados via API, armazenamento em banco de dados relacional e análises exploratórias e preditivas com modelos de aprendizado não supervisionado como **Isolation Forest** e **DBSCAN**.  
O projeto serve como uma base sólida para estudos e aplicações práticas em detecção de fraudes e padrões atípicos em dados transacionais de grande escala.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

<img width="293" height="684" alt="image" src="https://github.com/user-attachments/assets/3035b832-faae-4c3a-aa9e-62d81a3737ba" />


### Descrição dos Diretórios e Arquivos Principais

* **`data/`** — Contém os dados utilizados no projeto.  
  * `raw/`: Dados brutos coletados de fontes externas (como o Portal da Transparência e IBGE).  
  * `processed/`: Dados limpos e tratados, prontos para análise ou modelagem.

* **`main.py`** — Script principal responsável por orquestrar a coleta, o processamento e o salvamento dos dados no banco de dados.

* **`notebooks/`** — Contém notebooks Jupyter para análise exploratória e modelagem de anomalias:  
  * `1_data_preprocessing.ipynb`: Processamento e limpeza de dados, com criação de features e normalização.  
  * `2_Isolation_forest.ipynb`: Implementação e análise de anomalias com o modelo **Isolation Forest**.  
  * `3_DBSCAN.ipynb`: Aplicação do algoritmo **DBSCAN (Density-Based Spatial Clustering)** para detectar padrões e outliers com base em densidade.

* **`src/`** — Código-fonte da aplicação, modularizado em três camadas:
  * **`config/`** — Configurações gerais do sistema:
    * `api.py`: Configuração e chave de autenticação da API.  
    * `const.py`: Constantes e parâmetros fixos da aplicação.  
    * `database.py`: Conexão e configuração do banco de dados PostgreSQL.  
  * **`services/`** — Camada de serviços e integração com fontes externas:
    * `api_collector.py`: Lida com a coleta de dados do Portal da Transparência.  
    * `db_manager.py`: Manipula conexões, inserções e consultas ao banco de dados.  
  * **`utils/`** — Funções auxiliares de limpeza e manipulação:
    * `data_cleaning.py`: Limpeza, normalização e tratamento de dados.  
    * `number_utils.py`: Conversões de formatos numéricos brasileiros e padronização.

---

## Configuração e Uso

### Pré-requisitos

Antes de começar, é necessário ter instalado:
- **Python 3.8+**
- **PostgreSQL**  
- **pip** (gerenciador de pacotes Python)

Certifique-se de configurar corretamente as credenciais de banco e da API.

---

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/public-data-analysis-anomaly-detection-ml.git
   cd public-data-analysis-anomaly-detection-ml
Crie e ative um ambiente virtual (recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados:
Edite o arquivo src/config/database.py com as suas credenciais do PostgreSQL:

python
Copiar código
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "notas_db",
    "user": "postgres",
    "password": "postgres"
}
Configure a chave da API:
Edite o arquivo src/config/api.py:

python
Copiar código
API_KEY = "SUA_CHAVE_DA_API"
Execução
Para iniciar o processo de coleta e armazenamento de dados:

bash
Copiar código
python main.py
O script coleta os dados da API pública, processa e armazena as informações no banco de dados PostgreSQL, prontos para análise.

Análise de Dados e Modelagem
Após coletar e preparar os dados, utilize os notebooks para explorar e modelar as anomalias:

bash
Copiar código
jupyter notebook notebooks/
Os notebooks abordam:

Pré-processamento e limpeza dos dados.

Combinação de datasets (notas fiscais e dados demográficos).

Aplicação dos algoritmos Isolation Forest e DBSCAN.

Interpretação dos resultados e visualização de outliers.

Tecnologias e Bibliotecas Principais
Python 3.8+

Pandas — Manipulação de dados.

NumPy — Cálculos numéricos.

Scikit-learn — Modelagem e detecção de anomalias.

Matplotlib / Seaborn — Visualização de dados.

SQLAlchemy / psycopg2 — Integração com PostgreSQL.

Requests — Coleta de dados via API.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
