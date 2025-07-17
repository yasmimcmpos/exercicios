# Implemente operações básicas de lista.

# Em linguagens funcionais, liste operações como , , e são muito comuns.
# Implemente uma série de operações básicas de lista,
# sem usar funções existentes. length map reduce

# O número e os nomes exatos das operações a serem implementadas dependerão
# do controle para evitar conflitos com nomes existentes,
# mas as operações gerais que você implementará incluem:

# append (dadas duas listas, adicione todos os
# itens da segunda lista ao final da primeira lista);

# concatenate (dada uma série de listas, combine todos os itens em todas
# as listas em uma lista nivelada);

# filter (dado um predicado e uma lista, retorna a lista de todos os itens
# para os quais é Truepredicate(item));

# length (dada uma lista, retorna o número total de itens dentro dela);

# map (dada uma função e uma lista, retorna a lista dos resultados da aplicação
# em todos os itens function(item));

# foldl (Dada uma função, uma lista e um acumulador inicial, dobre (reduza)
# cada item no acumulador da esquerda);

# foldr (dada uma função, uma lista e um acumulador inicial, dobre (reduza)
# cada item no acumulador da direita);

# reverse (dada uma lista, retorna uma lista com todos os itens originais,
# mas na ordem inversa).

# Observe que a ordem na qual os argumentos são passados para as
# funções de dobra (, ) é significativa.
# foldl foldr

from typing import Any, Callable


def append(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    :param lista 1:
    :param lista 2:
    :return resultado da soma
    """
    resultado: list[int] = []
    for item in lista1:
        resultado += [item]  # += soma e atualiza o valor
    for item in lista2:
        resultado += [item]
    return resultado


def concatenate(listas: list[int]) -> list[int]:
    resultado: list[int] = []
    for sublista in listas:  # Pega cada lista
        for item in sublista:  # pega cada item
            resultado += [item]  # add item a lista
    return resultado


def filter(predicado: Callable[[int], bool], lista: list[int]) -> list[Any]:
    resultado = []
    for item in lista:
        if predicado(item):  # predicado testa cada item da lista
            resultado += [item]
    return resultado


def lenght(lista: list[int]):
    contador = 0
    for _ in lista:  # _ qualquer valor
        contador += 1  # percorre item a item, cada um achado soma 1 no contador
    return contador


def map(funcao: Callable[[int], int], lista: list[int]):
    resultado = []
    for item in lista:
        resultado += [funcao(item)]

    return resultado


def foldl(funcao: Callable[[int, int], int], acumulador: int, lista: list[int]):
    """Aplica uma função binária acumuladora da esquerda para a direita

    Args:
        funcao (Callable[[int, int], int]): Função que recebe acumulador e item
        retorna novo acumulador.
        acumulador (int): Valor inicial do acumulador.
        lista (list[int]): Lista de inteiros.

    Returns:
        int: Resultado final do acumulador
    """
    for item in lista:
        acumulador = funcao(acumulador, item)
        # exemplo soma(0, 1) --> 1
        # exemplo soma(1, 2) --> 3
        # exemplo soma(3, 3) --> 6
    return acumulador


def foldr(funcao, acumulador, lista: list[int]):
    if lista == []:
        return acumulador
    else:
        return funcao(lista[0], foldr(funcao, acumulador, lista[1:]))
        # vai combinando elementos de trás pra frente


def reverse(lista: list[int]):
    resultado = []
    for item in lista:
        resultado = [item] + resultado
        # coloca item no início, contrário do append
    return resultado
