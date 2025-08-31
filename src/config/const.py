consulta_sql = '''

SELECT "id",
       "orgaoDestinatario",
       "nomeFornecedor",
       "cnpjFornecedor",
       "municipioFornecedor",
       "valorNotaFiscal",
       "itensNotaFiscal",
       "tipoEventoMaisRecente",
       "dataEmissao",
       "eventosNotaFiscal",
       "chaveNotaFiscal"
FROM notas_fiscais;

'''