# Fatores Primos
# https://exercism.org/tracks/python/exercises/prime-factors
# Calcule os fatores primos de um determinado número natural.
# Roda bem para números até cerca de 10^12 – 10^14


def fatores_primos(valor: int) -> dict[int, int]:
    """Retorna a fatoração prima de um número natural n
    no formato {primo: expoente}.

    Args:
        valor: Número natural >= 1

    Returns:
        Dicionário com primos como chave e expoentes como valor

    Raises:
        ValueError: Se valor <= 0
    """
    if valor == 1:
        return {}

    if valor <= 0:
        raise ValueError("O número deve ser maior que 0.")

    fatores: dict[int, int] = {}

    while valor % 2 == 0:
        fatores[2] = fatores.get(2, 0) + 1
        valor //= 2

    divisor = 3

    while divisor <= valor // divisor:
        while valor % divisor == 0:
            fatores[divisor] = fatores.get(divisor, 0) + 1
            valor //= divisor
        divisor += 2

    if valor > 1:
        fatores[valor] = fatores.get(valor, 0) + 1

    return fatores
