# Um número palindrômico é lido da mesma forma nos dois sentidos.
# O maior palíndromo feito do produto de 2 números de dígitos é:
# 9009 = 91 x 99
# Encontre o maior palíndromo feito do produto de 3
# números de dígitos.


from itertools import combinations_with_replacement

# combinations_with_replacement cria todos os pares possíveis de
# números sem repetir ordem, ou seja, (123, 456) é o mesmo que (456, 123) —
# ele só usa um dos dois.
# Obs: já está no readme.md, só está aqui para explicar melhor.


def se_e_palindromo(n: int) -> bool:
    s = str(n)

    return s == s[::-1]  # slice invertido - a string invertida


# s[::-1] :: pega a string do inicio ao fim
# -1 = faz ele ir ao contrário


def maior_palindromo(tamanho: int) -> int:
    numeros = range(10 ** (tamanho - 1), 10**tamanho)
    # Gera os números possíveis desse tamanho

    produtos = (a * b for a, b in combinations_with_replacement(numeros, 2))
    # Gerador com todos os n possivei de (a * b)

    palindromos = filter(se_e_palindromo, produtos)
    # filtra para encontrar só os que são palindromos...

    return max(palindromos)
