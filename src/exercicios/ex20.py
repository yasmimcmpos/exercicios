# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
# Fazer o calculo para exibir o resultado/ depois o test


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for index in range(2, int(number**0.5) + 1):
        if not number % index:
            return False

    return True


def sum_primes(limit: int) -> int:
    total = 0
    for number in range(2, limit + 1):
        total += number
    return total
