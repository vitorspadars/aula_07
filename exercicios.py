from typing import List

valor: List = [5.0,7.0,8.0,10.0]
# 1. Calcular Média de Valores em uma Lista
# """
# Receba uma lista e retorna a média dela em float
# """
# def media_de_lista(valores: List[float]) -> float:
#     return sum(valores) / len(valores)

# resultado = media_de_lista(valor)

# print(resultado)


# Filtrar Dados Acima de um Limite

def filtrar_valores(limite: float, lista: List[float]):
    """
    Recebe um valor de corte e uma lista de valores, 
    retorna uma lista de valores maior do que o valor de corte
    """
    valores_filtrados: List[float] = []
    for i in lista:
        if i > limite:
            valores_filtrados.append(i)
    return valores_filtrados

resultados = filtrar_valores(7, valor)

print(resultados)