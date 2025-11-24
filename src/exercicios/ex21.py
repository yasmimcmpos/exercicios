# Exercism - Say: https://exercism.org/tracks/python/exercises/say

NUMEROS = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)

DECIMOS = (
    None,  # placehoders
    None,
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
)

ESCALAS = (
    (10**9, "billion"),
    (10**6, "million"),
    (10**3, "thousand"),
)


def tres_digitos(tres_digitos: int) -> str:
    """Converte um número de 0 a 999 em palavras.

    Args:
        n: Número inteiro entre 0 e 999

    Returns:
        String com o número por extenso em inglês
    """
    palavras: list[str] = []
    centenas, resto = divmod(tres_digitos, 100)

    if centenas:
        palavras.append(NUMEROS[centenas])
        palavras.append("hundred")

    if resto:
        if resto < 20:
            palavras.append(NUMEROS[resto])

        else:
            dezenas, unidades = divmod(resto, 10)

            if unidades:
                palavras.append(f"{DECIMOS[dezenas]}-{NUMEROS[unidades]}")

            else:
                palavras.append(DECIMOS[dezenas])

    return " ".join(palavras)


def say(value: int) -> str:
    """Converte números de 0 a 999.999.999.999 em palavras.

    Args:
        n: Número inteiro a ser convertido

    Returns:
        String com o número por extenso em inglês

    Raises:
        ValueError: Se o número não for inteiro ou estiver fora do intervalo

    Examples:
        >>> say(0)
        'zero'
        >>> say(42)
        'forty-two'
        >>> say(1234)
        'one thousand two hundred thirty-four'
    """
    if value < 0 or value > 999_999_999_999:
        raise ValueError("input out of range")

    if not value:  # +intuitivo
        return "zero"

    if value < 1_000:
        return tres_digitos(value)

    palavras: list[str] = []

    for valor_escala, nome_escala in ESCALAS:
        if value >= valor_escala:
            grupo, value = divmod(value, valor_escala)
            palavras.append(tres_digitos(grupo))
            palavras.append(nome_escala)

    if value > 0:
        palavras.append(tres_digitos(value))

    return " ".join(palavras)
