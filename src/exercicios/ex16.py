# # What is the 10_001st prime number?


def is_prime(number: int) -> bool:
    """Check if a number n is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
    """
    if number < 2:
        return False

    for index in range(2, int(number**0.5) + 1):
        if not number % index:
            return False

    return True


def find_prime_at_position(target_position: int) -> int:
    """Find the prime number at the given position in the sequence of primes.
    Example: position 6 -> 13
    """
    count = 0
    possible_prime = 1

    while count < target_position:
        possible_prime += 1
        if is_prime(possible_prime):
            count += 1

    return possible_prime
