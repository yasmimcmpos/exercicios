from exercicios.ex14 import RationalNumber


def test_add() -> None:
    assert RationalNumber(1, 2) + RationalNumber(1, 3) == (5, 6)


def test_sub() -> None:
    assert RationalNumbers(3, 4) - RationalNumbers(1, 4) == RationalNumbers(1, 2)
