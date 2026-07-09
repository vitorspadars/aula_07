import csv

path_arquivo = 'vendas.csv'

def ler_csv(nome_arquivo: str) -> list[dict]:
    with open(nome_arquivo, mode='r', encoding='utf-8', ) as file:
        leitor = csv.DictReader(file)
        return list(leitor)

# vendas_itens: list[dict] = []

# vendas_itens = ler_csv(path_arquivo)
# print(vendas_itens)


def processar_dados(dados: list[dict]) -> dict:
    categorias: dict = {}
    for item in dados:
        categoria = item["Categoria"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

def calcular_vendas_categorias(dados_processados: dict) -> dict:
    vendas_por_categoria = {}

    for categoria, itens in dados_processados.items():
        total_de_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_de_vendas
    return vendas_por_categoria