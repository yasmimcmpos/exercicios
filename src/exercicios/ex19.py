# Fatores Primos
# https://exercism.org/tracks/python/exercises/prime-factors
# Calcule os fatores primos de um determinado número natural.
# Roda bem para números até cerca de 10^12 – 10^14


def fatores_primos(n: int) -> list[int]:
    """Retorna uma lista com os fatores primos de um número natural n.
    Otimizado para números grandes.

    Args:
        n: Número natural maior que 1

    Returns:
        Lista de fatores primos em ordem crescente

    Raises:
        ValueError: Se n <= 1
    """
    if n <= 1:
        raise ValueError("O número deve ser maior que 1.")

    fatores: list[int] = []

    while n % 2 == 0:
        fatores.append(2)
        n //= 2

    divisor = 3

    while divisor <= n // divisor:  # só verifica até raiz de n
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 2

    if n > 1:
        fatores.append(n)

    return fatores
