# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.


def is_prime(number: int) -> bool:
    """Calculate if the number is prime

    Args:
        number (int): numbers to be calculated

    Returns:
        bool: True - If is a prime number
    """
    if number < 2:
        return False

    for index in range(2, int(number**0.5) + 1):
        if not number % index:
            return False

    return True


def sum_primes(limit: int) -> int:
    """Sum of the primes numbers

    Args:
        limit (int): When one needs to stop the sum

    Returns:
        int: The sum of the total the prime numbers up to the limit
    """
    total = 0
    for number in range(2, limit + 1):
        if is_prime(number):
            total += number

    return total
