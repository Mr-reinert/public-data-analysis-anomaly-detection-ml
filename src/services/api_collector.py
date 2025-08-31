# Funções para coletar dados da API.

from src.config.api import HEADERS, BASE_URL_NF, BASE_URL_CHNF
from src.services.db_manager import save_to_postgres
from typing import List, Dict, Any
import pandas as pd
import requests
import time



def fetch_notes(code: str, page: int) -> List[Dict[str, Any]]:
    """
    Busca uma página de notas fiscais da API.
    """
    params = {"codigoOrgao": code, "pagina": page}
    try:
        response = requests.get(BASE_URL_NF, headers=HEADERS, params=params, timeout=(10, 120))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        return []

def fetch_note_details(note: Dict[str, Any]) -> Dict[str, Any]:
    """
    Busca informações detalhadas para uma nota fiscal específica usando sua chave.
    """
    key = note.get("chaveUnicaNotaFiscal") or note.get("chaveNotaFiscal")
    if not key:
        return note

    params = {"chaveUnicaNotaFiscal": key}
    try:
        response = requests.get(BASE_URL_CHNF, headers=HEADERS, params=params, timeout=(10, 60))
        response.raise_for_status()
        note.update(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for key {key}: {e}")
    finally:
        time.sleep(0.3)
    return note

def collect_data(code: str, table: str, start_page: int = 1, end_page: int = 1221) -> None:
    """
    Coleta dados da API, incluindo os detalhes de cada nota fiscal,
    e salva no banco de dados página por página.
    
    """

    for page in range(start_page, end_page + 1):
        page_data = fetch_notes(code, page)
        if not page_data:
            print(f"Fim dos dados na página {page}.")
            break

        print(f"Processando a página {page} com {len(page_data)} registros...")
        
        detailed_data = [fetch_note_details(note) for note in page_data]
        
        df = pd.json_normalize(detailed_data, sep=".")
        
        save_to_postgres(df, table)
        
        time.sleep(0.5)