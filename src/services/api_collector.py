# Funções para coletar dados da API - versão otimizada
from src.config.api import HEADERS, BASE_URL_NF, BASE_URL_CHNF
from src.services.db_manager import save_to_postgres
from typing import List, Dict, Any
import pandas as pd
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_RETRIES = 3        # Número máximo de tentativas para cada requisição
PAGE_WORKERS = 5       # Número de threads para buscar PÁGINAS
DETAILS_WORKERS = 15   # Número de threads para buscar DETALHES

def fetch_notes(session: requests.Session, code: str, page: int, retries: int = MAX_RETRIES) -> List[Dict[str, Any]]:
    """Busca uma página de notas fiscais da API usando uma session."""
    params = {"codigoOrgao": code, "pagina": page}
    
    for attempt in range(1, retries + 1):
        try:
            response = session.get(BASE_URL_NF, params=params, timeout=(5, 60))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ReadTimeout:
            print(f"Timeout na página {page} (tentativa {attempt}/{retries}).")
            time.sleep(5 * attempt)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar página {page}: {e}")
            break
    
    print(f"Falha definitiva na página {page} após {retries} tentativas.")
    return []

def fetch_note_details(session: requests.Session, note: Dict[str, Any], retries: int = MAX_RETRIES) -> Dict[str, Any]:
    """Busca detalhes de uma nota fiscal usando uma session."""
    key = note.get("chaveUnicaNotaFiscal") or note.get("chaveNotaFiscal")
    if not key:
        return note

    params = {"chaveUnicaNotaFiscal": key}
    
    for attempt in range(1, retries + 1):
        try:
            # Usando session.get()
            response = session.get(BASE_URL_CHNF, params=params, timeout=(5, 60))
            response.raise_for_status()
            note.update(response.json())
            return note
        except requests.exceptions.ReadTimeout:
            print(f"Timeout ao buscar detalhes da chave {key} (tentativa {attempt}/{retries})")
            time.sleep(3 * attempt)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar detalhes da chave {key}: {e}")
            break
            
    print(f"Falha definitiva ao buscar detalhes da chave {key} após {retries} tentativas.")
    return note

def process_page(session: requests.Session, code: str, page: int) -> pd.DataFrame:
    """Função que encapsula todo o processamento de uma única página."""
    page_data = fetch_notes(session, code, page)
    if not page_data:
        print(f"Fim dos dados ou erro na página {page}.")
        return pd.DataFrame() # Retorna DataFrame vazio se não houver dados

    print(f"📄 Página {page} obtida com {len(page_data)} registros. Buscando detalhes...")

    detailed_data = []
    with ThreadPoolExecutor(max_workers=DETAILS_WORKERS) as details_executor:
        # Passa a session para a função de buscar detalhes
        future_to_note = {details_executor.submit(fetch_note_details, session, note): note for note in page_data}
        for future in as_completed(future_to_note):
            detailed_data.append(future.result())

    print(f"✅ Detalhes da página {page} processados.")
    return pd.json_normalize(detailed_data, sep=".")

def collect_data(code: str, table: str, start_page: int = 1, end_page: int = 30996) -> None:
    """
    Coleta dados da API de forma massivamente paralela e salva no banco de dados.
    """
    # Cria uma única session para reutilizar conexões
    with requests.Session() as session:
        session.headers.update(HEADERS)  # Adiciona os headers na session

        # Executor principal para buscar e processar PÁGINAS
        with ThreadPoolExecutor(max_workers=PAGE_WORKERS) as page_executor:
            # Submete todas as tarefas de processamento de página de uma vez
            future_to_page = {
                page_executor.submit(process_page, session, code, page): page
                for page in range(start_page, end_page + 1)
            }

            # Processa os resultados conforme eles ficam prontos
            for future in as_completed(future_to_page):
                page_num = future_to_page[future]
                try:
                    df = future.result()
                    if not df.empty:
                        print(f"Salvando dados da página {page_num} no banco...")
                        save_to_postgres(df, table)
                        print(f"Dados da página {page_num} salvos.")
                except Exception as exc:
                    print(f"Página {page_num} gerou uma exceção: {exc}")