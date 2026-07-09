from etl import ler_csv, processar_dados, calcular_vendas_categorias

path_arquivo = 'vendas.csv'

dados_brutos = ler_csv(path_arquivo)
dados_tratados = processar_dados(dados_brutos)
vendas = calcular_vendas_categorias(dados_tratados)

print(vendas)