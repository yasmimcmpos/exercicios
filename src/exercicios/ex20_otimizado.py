# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
# Version 2 - For a better optimized version of the exercise


def is_prime(number: int) -> bool:
    """Calculate if the number is prime

    Args:
        number (int): numbers to be calculated

    Returns:
        bool: True - If is a prime number

    Observations:
    #Como não tem numero primo par além do 2, então:
    #Podemos testar primeiro o 2,
    #Depois testa só os impares a partir do 3 de dois em dois
    """
    if not number % 2:
        return False

    for index in range(3, int(number**0.5) + 1, 2):
        if not number % index:
            return False

    return True


def sum_primes(limit: int) -> int:
    """Sum of the primes numbers

    Args:
        limit (int): When one needs to stop the sum

    Returns:
        int: The sum of the total the prime numbers up to the limit
    Observations:
    #Começa pelo 2
    #Testa só os impares a partir do 3 de dois em dois
    """
    total = 2
    for number in range(3, limit + 1, 2):
        if is_prime(number):
            total += number

    return total
