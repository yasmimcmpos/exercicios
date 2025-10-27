# Fatores Primos
# https://exercism.org/tracks/python/exercises/prime-factors
# Calcule os fatores primos de um determinado número natural.
# Roda bem para números até cerca de 10^12 – 10^14


def fatores_primos(valor: int) -> list[int]:
    """Retorna uma lista com os fatores primos de um número natural n.
    Otimizado para números grandes.

    Args:
        n: Número natural maior que 1

    Returns:
        Lista de fatores primos em ordem crescente

    Raises:
        ValueError: Se n <= 1
    """
    if valor <= 1:
        raise ValueError("O número deve ser maior que 1.")

    fatores: list[int] = []

    while not valor % 2:  # Evitar fazer comparação com 0 - Mais comum no python
        fatores.append(2)
        valor //= 2

    divisor = 3

    while divisor <= valor // divisor:  # só verifica até raiz de n
        while valor % divisor == 0:
            fatores.append(divisor)
            valor //= divisor
        divisor += 2

    if 1 < valor:  # melhor para linguagens de baixo nivel
        fatores.append(valor)

    return fatores
