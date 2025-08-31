import pandas as pd
import unidecode
def normalize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte todas as colunas de texto (object/string) para maiúsculas
    e remove acentos/caracteres especiais.

    """
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="object").columns:
        df_copy[col] = df_copy[col].astype(str).apply(
            lambda x: unidecode.unidecode(x.upper()) if pd.notnull(x) else x
        )
    return df_copy