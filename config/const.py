consulta_sql = '''

SELECT "id",
       "orgaoDestinatario",
       "nomeFornecedor",
       "cnpjFornecedor",
       "municipioFornecedor",
       "itensNotaFiscal",
       "tipoEventoMaisRecente",
       "dataEmissao",
       "eventosNotaFiscal",
       "chaveNotaFiscal"
FROM notas_fiscais;

'''