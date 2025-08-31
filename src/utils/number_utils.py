import pandas as pd

def br_to_float(x):
    if pd.isna(x):
        return 0
    # Remove tudo que não for dígito
    x = ''.join(filter(str.isdigit, str(x)))
    if len(x) < 3:  # Se tiver menos de 3 dígitos, considera tudo decimal
        return float(x) / 100
    # Insere o ponto antes dos dois últimos dígitos
    x = x[:-2] + '.' + x[-2:]
    return float(x)