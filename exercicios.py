# 1. Calcular Média de Valores em uma Lista

from typing import List

valor: List = [5.0,7.0,8.0,10.0]
"""
Receba uma lista e retorna a média dela em float
"""
def media_de_lista(valores: List[float]) -> float:
    return sum(valores) / len(valores)

resultado = media_de_lista(valor)

print(resultado)