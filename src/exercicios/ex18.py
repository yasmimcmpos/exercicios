# Trigêmeo pitagórico especial - https://projecteuler.net/problem=9
# Um trigêmeo pitagórico é um conjunto de três números naturais, a < b< c
# para os quais


def verificar_trigemeo(
    a: int,
    b: int,
    c: int,
) -> bool:
    """Verifica se três números formam um trígêmeo pitagórico.

    Um trígêmeo pitagórico é um conjunto de três números inteiros positivos
    que satisfazem o teorema de Pitágoras: a² + b² = c².

    Args:
        a: Primeiro cateto do triângulo retângulo.
        b: Segundo cateto do triângulo retângulo.
        c: Hipotenusa do triângulo retângulo.

    Returns:
        True se a² + b² = c², False caso contrário.

    Examples:
        >>> verificar_trigemeo(3, 4, 5)
        True
        >>> verificar_trigemeo(5, 12, 13)
        True
        >>> verificar_trigemeo(1, 2, 3)
        False
    """

    return a**2 + b**2 == c**2


def encontrar_trigemeo_pitagorico(soma_alvo: int) -> tuple[int, int, int]:
    """Encontra um trígêmeo pitagórico cuja soma seja igual ao valor alvo.

    Busca três números inteiros positivos a, b e c onde:
    - a² + b² = c² (teorema de Pitágoras)
    - a + b + c = soma_alvo
    - a < b < c

    Args:
        soma_alvo: Valor inteiro positivo que representa a soma desejada
                   dos três números do trígêmeo.

    Returns:
        Tupla (a, b, c) contendo o trígêmeo pitagórico encontrado, onde
        a < b < c. Retorna (0, 0, 0) se nenhum trígêmeo for encontrado.

    """

    for a in range(1, soma_alvo // 3):  # a < b< c
        for b in range(a + 1, soma_alvo // 2):
            c = soma_alvo - a - b

            if c <= b:
                continue

            if verificar_trigemeo(a, b, c):
                return a, b, c

    return (0, 0, 0)
