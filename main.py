# Arquivo Principal

from services.api_collector import collect_data
from services.db_manager import save_to_postgres

def main():
    """
    Função principal para orquestrar o processo de coleta e salvamento de dados.
    """
    code = "36000"
    table = "notas_fiscais"
    total_pages = 3

    print(f"Iniciando a coleta de dados para o código {code}...")

    # A função collect_data agora lida com o salvamento por conta própria
    collect_data(code, table, end_page=total_pages)

    print("Coleta e salvamento finalizados.")

if __name__ == "__main__":
    main()