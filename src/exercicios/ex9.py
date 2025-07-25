# ===MMC===
# 2520  is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
# Logic:
# Função 1:
# Calcular o MMC de dois em dois, calcula dois e passa para o próximo

# Função 2:
# Criar uma lista e aplicar o MMC nela para todos os números

import math
from functools import reduce


def calc_mmc(a: int, b: int) -> int:
    """calculo de mmc

    Args:
        a (int): primeiro número a ser multiplicado
        b (int): segundo número a ser multiplicado

    Returns:
        int: resultado do MMC inteiro

    Observations:
       -A função 'abs' garante que o resultado seja positivo
       -A função 'math.gcd' calcula o máximo divisor comum entre dois numeros

    """
    return abs(a * b) // math.gcd(a, b)


def mmc_in_list(lista: list[int]) -> int:
    """Calcular o MMC dentro da lista

    Args:
        lista (list[int]): Lista de 1 a 10

    Returns:
        int: acumulo dos MMcs de todos os num da lista

    Observations:
        -A função 'reduce' pega os dois primeiro num e vai multiplicando-os
        cumulativamente com os seguintes da sequência.

    """
    return reduce(calc_mmc, lista)
