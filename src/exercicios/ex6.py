# Um número palindrômico é lido da mesma forma nos dois sentidos.
# O maior palíndromo feito do produto de 2 números de dígitos é:
# 9009 = 91 x 99
# Encontre o maior palíndromo feito do produto de 3
# números de dígitos.


from itertools import combinations_with_replacement


def se_e_palindromo(valor: int) -> bool:
    string = str(valor)

    return "".join(reversed(string)) == string
    # "".join junta as strings


def maior_palindromo(tamanho: int) -> int:
    n_digitos = range(10 ** (tamanho - 1), 10**tamanho)
    # numeros = [1,...,9] = 1
    # numeros = [10,...,99]  =2
    # numeros = [100,...,999] =3
    # Gera os números possíveis desse tamanho

    produtos = (a * b for a, b in combinations_with_replacement(n_digitos, 2))
    # Gerador com todos os n possivei de (a * b)

    palindromos = [x for x in produtos if se_e_palindromo(x)]
    # Forma mais Pythonista de fazer
    # palindromos = filter(se_e_palindromo, produtos)

    return max(palindromos)
