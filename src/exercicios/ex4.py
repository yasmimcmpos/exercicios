# Encontre a diferença entre o quadrado da soma e a soma dos quadrados dos
# primeiros N números naturais

# O quadrado da soma dos dez primeiros números naturais é:
# (1 + 2 + ... + 10)² = 55² = 3025

# A soma dos quadrados dos dez primeiros números naturais é:
# 1² + 2² + ... + 10² = 385

# Portanto, a diferença entre o quadrado da soma dos dez primeiros
# números naturais e a soma dos quadrados dos dez primeiros números naturais é
# 3025 - 385 = 2640


def diferenca_quadrados(n: int) -> int:
    return sum(range(1, n + 1)) ** 2 - sum(i**2 for i in range(1, n + 1))
