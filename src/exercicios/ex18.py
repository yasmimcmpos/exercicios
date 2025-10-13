def verificar_trigemeo(
    a: int,
    b: int,
    c: int,
) -> bool:
    return a**2 + b**2 == c**2


def encontrar_trigemeo_pitagorico(soma_alvo: int) -> tuple[int, int, int] | None:
    for a in range(1, soma_alvo // 3):
        for b in range(a + 1, soma_alvo // 2):
            c = soma_alvo - a - b

            if c <= b:
                continue

            if verificar_trigemeo(a, b, c):
                return a, b, c

    return None
