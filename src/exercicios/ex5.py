# Os Fatores Primos de 13195 são 5, 7, 13, 29
# Qual é o maior fator primo do número 6008514751413?
# Função deve dividir meu numero por todos os numeros primos até não sobrar mais

# Obs.: Maior dificuldade na hora dos testes é a matemática


def maior_fator_primo(n: int) -> int:
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n //= i
    return n
