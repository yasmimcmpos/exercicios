# Cada novo termo na sequência de Fibonacci é gerado pela soma dos dois termos anteriores.
# Começando com 1 e 2, os primeiros 10 termos serão:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Considerando os termos na sequência de Fibonacci cujos valores não excedem quatro milhões,
# encontre a soma dos termos de valor par.


def pares_e_soma(limite: int) -> int:
    """Essa função faz a soma de Fibonacci até o limite dado

    Args:
        limite (int): _description_

    Returns:
        int: o valor da soma
    """
    a = 1
    b = 2
    soma = 0

    while a <= limite:
        if a % 2 == 0:
            soma += a
        a, b = b, a

    return soma
