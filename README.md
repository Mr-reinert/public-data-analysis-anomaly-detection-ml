# Análise de Dados Públicos e Detecção de Anomalias com Machine Learning

Este projeto tem como objetivo principal coletar, processar e analisar dados públicos relacionados a notas fiscais, com foco na detecção de anomalias. Ele serve como uma base robusta para futuras implementações de modelos de Machine Learning para identificar padrões incomuns ou fraudulentos em grandes volumes de dados transacionais.




## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── LICENSE
├── README.md
├── data
│   ├── processed
│   │   ├── itens_notas_fiscais.csv
│   │   └── notas_fiscais.csv
│   └── raw
│       └── ibge_municipios.csv
├── main.py
├── notebooks
│   └── data_preprocessing.ipynb
├── requirements.txt
└── src
    ├── __init__.py
    ├── config
    │   ├── __init__.py
    │   ├── api.py
    │   ├── const.py
    │   └── database.py
    ├── services
    │   ├── __init__.py
    │   ├── api_collector.py
    │   └── db_manager.py
    └── utils
        ├── __init__.py
        ├── data_cleaning.py
        └── number_utils.py
```

### Descrição dos Diretórios e Arquivos Principais:

*   `data/`: Contém os dados utilizados no projeto.
    *   `raw/`: Dados brutos, como `ibge_municipios.csv` (dados populacionais do IBGE).
    *   `processed/`: Dados processados e limpos, como `itens_notas_fiscais.csv` e `notas_fiscais.csv`.
*   `main.py`: O ponto de entrada principal da aplicação, responsável por orquestrar a coleta e o salvamento dos dados da API.
*   `notebooks/`: Contém notebooks Jupyter para análise exploratória de dados (EDA) e pré-processamento.
    *   `data_preprocessing.ipynb`: Notebook detalhado que demonstra as etapas de pré-processamento, limpeza e engenharia de features dos dados.
*   `requirements.txt`: Lista as dependências Python necessárias para o projeto.
*   `src/`: Contém o código-fonte da aplicação, organizado em módulos.
    *   `config/`: Módulos de configuração.
        *   `api.py`: Configurações relacionadas à API, como chaves e URLs base.
        *   `const.py`: Constantes e variáveis globais, como a consulta SQL padrão.
        *   `database.py`: Configurações de conexão com o banco de dados PostgreSQL.
    *   `services/`: Módulos que implementam a lógica de negócio e interação com serviços externos.
        *   `api_collector.py`: Funções para coletar dados da API do Portal da Transparência.
        *   `db_manager.py`: Funções para gerenciar a conexão e operações com o banco de dados PostgreSQL.
    *   `utils/`: Módulos com funções utilitárias.
        *   `data_cleaning.py`: Funções para limpeza e normalização de dados.
        *   `number_utils.py`: Funções utilitárias para manipulação de números (ex: conversão de formatos brasileiros para float).



## Configuração e Uso

Para configurar e executar este projeto, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado, bem como o `pip` para gerenciamento de pacotes. Além disso, é necessário ter uma instância do PostgreSQL em execução e acessível com as credenciais configuradas em `src/config/database.py`.

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/public-data-analysis-anomaly-detection-ml.git
    cd public-data-analysis-anomaly-detection-ml
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o banco de dados:**

    Atualize o arquivo `src/config/database.py` com as suas credenciais do PostgreSQL. Certifique-se de que o banco de dados (`notas_db` por padrão) exista ou crie-o.

    ```python
    # src/config/database.py
    DB_CONFIG = {
        "host": "localhost",
        "port": 5432,
        "dbname": "notas_db",
        "user": "postgres",
        "password": "postgres"
    }
    ```

5.  **Configure a chave da API:**

    Obtenha uma chave da API do Portal da Transparência e atualize o arquivo `src/config/api.py`.

    ```python
    # src/config/api.py
    API_KEY = "SUA_CHAVE_DA_API"
    # ... outras configurações
    ```

### Execução

Para iniciar a coleta de dados e salvá-los no banco de dados, execute o script principal:

```bash
python main.py
```

Este script coletará dados de notas fiscais da API do Portal da Transparência e os armazenará no PostgreSQL. A quantidade de páginas a serem coletadas pode ser ajustada em `main.py`.

### Análise e Pré-processamento de Dados

Para explorar e pré-processar os dados, utilize o notebook Jupyter:

```bash
jupyter notebook notebooks/data_preprocessing.ipynb
```

Este notebook detalha as etapas de:

*   Carregamento de dados do PostgreSQL.
*   Tratamento e junção de dados demográficos (IBGE).
*   Engenharia de features e ajustes finais, incluindo limpeza e normalização de colunas, conversão de tipos de dados e criação de tabelas auxiliares para itens de notas fiscais.



## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.