# # What is the 10_001st prime number?

# # Calcular os numeros primos
# # percorrer todos os primos até a posição 10001
# # dizer qual é o numero da posição
# # Para isso, teste se ele não é divisível por nenhum número entre 2 e a
# # raiz quadrada dele

# #Mantenha uma contagem de quantos primos você encontrou.

# Toda vez que encontrar um primo, aumente a contagem.

# Quando chegar no 10.001º primo, pare e guarde esse número.


class PositionPrimeNumber:
    def __init__(self, prime: int) -> None:
        self.prime = prime

    def is_prime(self, num):
        # verificar s é primo

    def find_prime(self, nth):
        # encontra a posição 10001 do primo