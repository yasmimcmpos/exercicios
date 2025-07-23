# Os Fatores Primos de 13195 são 5, 7, 13, 29
# Qual é o maior fator primo do número 600851475143?
# Função deve dividir meu numero por todos os numeros primos até não sobrar mais


def maior_fator_primo(n: int) -> int:
    maior = 0
    fatores = []
    temp = n

    for i in range(2, int(n**0.5) + 1):
        while temp % i == 0:
            temp //= i
            fatores.append(i)

        # if temp > 1:
        #     fatores.append(temp)

    maior = max(fatores)

    return maior
