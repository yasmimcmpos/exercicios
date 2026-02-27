from exercicios.ex24 import first_triangular_with_more_than


def test_simples() -> None:
    assert first_triangular_with_more_than(5) == 28


def test_find_first_over_500_divisors() -> None:
    assert first_triangular_with_more_than(500) == 76_576_500
