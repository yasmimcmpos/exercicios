from exercicios.ex14 import RationalNumber


def test_add() -> None:
    assert RationalNumber(1, 2) + RationalNumber(1, 3) == RationalNumber(5, 6)


def test_sub() -> None:
    assert RationalNumber(3, 4) - RationalNumber(1, 4) == RationalNumber(1, 2)


def test_mul() -> None:
    assert RationalNumber(2, 3) * RationalNumber(3, 4) == RationalNumber(1, 2)


def test_div() -> None:
    assert RationalNumber(1, 2) / RationalNumber(1, 4) == RationalNumber(2, 1)


def test_abs() -> None:
    assert abs(RationalNumber(-3, 4)) == RationalNumber(3, 4)


def test_pow_integer() -> None:
    assert RationalNumber(2, 3).pow_integer(2) == RationalNumber(4, 9)


def test_pow_real() -> None:
    result = RationalNumber(4, 9).pow_real(0.5)
    expected = (4**0.5) / (9**0.5)
    assert abs(result - expected) < 1e-9


def test_real_pow_rational() -> None:
    r = RationalNumber(1, 2)
    result = RationalNumber.real_pow_rational(9, r)
    expected = (9**1) ** (1 / 2)
    assert abs(result - expected) < 1e-9
