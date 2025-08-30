# Funções para interagir com o banco de dados.

import psycopg2
from psycopg2.extras import execute_values
from config.database import DB_CONFIG
import pandas as pd

def save_to_postgres(df: pd.DataFrame, table_name: str):
    """
    Salva os dados em uma tabela.
    """
    for col in df.columns:
        df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (dict, list)) else x)

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        columns = ", ".join([f'"{c}" TEXT' for c in df.columns])
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')

        records = df.values.tolist()
        cols = ", ".join([f'"{c}"' for c in df.columns])
        query = f"INSERT INTO {table_name} ({cols}) VALUES %s"
        execute_values(cur, query, records)

        conn.commit()
        print(f"{len(df)} records saved to {table_name}.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
    finally:
        if 'conn' in locals() and conn:
            cur.close()
            conn.close()


def fetch_data_from_db(sql_query: str) -> pd.DataFrame:
    """
    Executa uma consulta SQL no banco de dados e retorna os resultados em um DataFrame do Pandas.
    
    """
    con = None
    df = pd.DataFrame()

    try:
        # A conexão é estabelecida diretamente usando o dicionário DB_CONFIG importado
        con = psycopg2.connect(**DB_CONFIG)
        cursor = con.cursor()
        
        cursor.execute(sql_query)
        
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)
        
    except (psycopg2.Error, ValueError) as e:
        print(f"Erro ao executar a consulta ou conectar ao banco de dados: {e}")
        
    finally:
        # Garante que a conexão seja sempre fechada, mesmo se ocorrer um erro
        if con:
            con.close()
            
    return df