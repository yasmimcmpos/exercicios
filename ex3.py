#Cada novo termo na sequência de Fibonacci é gerado pela soma dos dois termos anteriores.
#Começando com 1 e 2, os primeiros 10 termos serão:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#Considerando os termos na sequência de Fibonacci cujos valores não excedem quatro milhões,
#encontre a soma dos termos de valor par.

def pares_e_soma(limite):
    a = 1
    b = 2
    soma = 0

    while a <= limite:
        if a % 2 == 0:
            soma += a
        a, b = b, a + b
    return soma

limite = 4000000
resultado = pares_e_soma(limite)
print(f"Somar os termos pares até {limite}: {resultado}")
