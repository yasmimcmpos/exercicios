# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
# Fazer o calculo para exibir o resultado/ depois o test


class sum_primes:
    def __init__(self, prime:int) -> None:
        self.prime = prime

    def calc_prime_numbers(self, number:int) -> None:
        for number in range(2,10):
            if 0 == i % 1 or 0 == i % i: