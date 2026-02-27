# https://projecteuler.net/problem=12
# Find the value of the first triangle number to have over five hundred divisors

from math import prod

from exercicios.ex19 import fatores_primos


def number_of_divisors(prime_factors: dict[int, int]) -> int:
    """
    Calcula o número total de divisores de um número a partir
    da sua fatoração prima.

    Args:
        prime_factors (dict): Dicionário contendo os fatores primos como chave
        e seus respectivos expoentes como valor.

    Returns:
        int: Quantidade total de divisores positivos do número.
    """
    return prod(exponent + 1 for exponent in prime_factors.values())


def first_triangular_with_more_than(min_divisors: int) -> int:
    """
    Encontra o primeiro número triangular que possui mais do que
    'min_divisors' divisores.

    Args:
        min_divisors (int): Número mínimo de divisores desejado.

    Returns:
        int: O primeiro número triangular com mais do que
        'min_divisors' divisores.

    Exemplos:
    n for par a = n//2, enquanto b = n+1
    n for impar a = n, então b = (n+1)//2

    """
    n = 1

    while True:
        # Como fazer sem while true
        if n % 2 == 0:
            a, b = n // 2, n + 1
        else:
            a, b = n, (n + 1) // 2

        total_divisors = number_of_divisors(fatores_primos(a)) * number_of_divisors(
            fatores_primos(b)
        )

        if total_divisors > min_divisors:
            return n * (n + 1) // 2

        n += 1
