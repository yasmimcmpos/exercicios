from exercicios.ex24 import primeiro_triangular_com_mais_de


def test_find_first_over_500_divisors() -> None:
    assert primeiro_triangular_com_mais_de(500) == 76576500
