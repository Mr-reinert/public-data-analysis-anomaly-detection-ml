consulta_sql = '''

SELECT "chaveNotaFiscal",
       "orgaoDestinatario",
       "nomeFornecedor",
       "cnpjFornecedor",
       "municipioFornecedor",
       "itensNotaFiscal",
       "tipoEventoMaisRecente",
       "dataEmissao",
       "eventosNotaFiscal"
FROM notas_fiscais;

'''