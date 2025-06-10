from exercicios.ex3 import pares_e_soma


def test_exemplo() -> None:
    assert 231 == pares_e_soma(90)


def test_esperado() -> None:
    assert 4613732 == pares_e_soma(4_000_000)
