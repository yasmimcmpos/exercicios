from exercicios.ex20 import sum_primes


def test_sum_primes() -> None:
    assert sum_primes(10) == 17
    assert sum_primes(2_000_000) == 142_913_828_922
