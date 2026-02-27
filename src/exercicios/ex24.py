# https://projecteuler.net/problem=12
# Find the value of the first triangle number to have over five hundred divisors

from exercicios.ex19 import fatores_primos


def quantidade_divisores(fatores: dict) -> int:
    total = 1
    for expoente in fatores.values():
        total *= expoente + 1
    return total


def primeiro_triangular_com_mais_de(min_divisores: int) -> int:
    n = 1

    while True:
        # Estratégia otimizada
        if n % 2 == 0:
            a = n // 2
            b = n + 1
        else:
            a = n
            b = (n + 1) // 2

        fatores_a = fatores_primos(a)
        fatores_b = fatores_primos(b)

        # Combinar fatorações (porque são coprimos)
        fatores_totais = fatores_a.copy()
        for primo, expoente in fatores_b.items():
            fatores_totais[primo] = fatores_totais.get(primo, 0) + expoente

        total_divisores = quantidade_divisores(fatores_totais)

        if total_divisores > min_divisores:
            return n * (n + 1) // 2

        n += 1
