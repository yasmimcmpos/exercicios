#Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. 
# A soma desses múltiplos é 23. Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.


def calculo(limite):
    soma = 0

    for i in range(1, limite):
        if 0 == i % 3 or 0 == i % 5:
            print(f"3 ou 5 = {i}")
            soma += i

    print(f"soma = {soma}")

calculo(1000)