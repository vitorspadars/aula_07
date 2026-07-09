from typing import List

valor: List = [5, 5, 7, 8, 8, 8, 10, 15]
# 1. Calcular Média de Valores em uma Lista

def media_de_lista(valores: List[float]) -> float:
    """
    Receba uma lista e retorna a média dela em float
    """
    return sum(valores) / len(valores)



# 2. Filtrar Dados Acima de um Limite

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

# 3. Contar Valores Únicos em uma Lista

def contador_de_valores_unicos(lista: List[float]) -> int:

    valores_unicos = len(set(lista))
    return valores_unicos


# 4. Converter Celsius para Fahrenheit em uma Lista

def conversor_celsius_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    fahrenheit = [(9/5) * temp + 32 for temp in temperaturas_celsius]
    return fahrenheit

# 5. Calcular Desvio Padrão de uma Lista

def desvio_padrao_lista(lista: List[float]) -> float:
    media_valores: float = sum(lista) / len(lista)
    variancia_valores: float = sum((x - media_valores) ** 2 for x in lista) / len(lista)
    resultado: float = variancia_valores ** 0.5
    return round(resultado, 2)

# 6. Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))