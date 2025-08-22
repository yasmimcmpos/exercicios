from exercicios.ex13 import ComplexNumber


def test_add() -> None:
    assert ComplexNumber(1, 2) + ComplexNumber(3, 4) == ComplexNumber(4, 6)


def test_sub() -> None:
    assert ComplexNumber(1, 2) - ComplexNumber(3, 4) == ComplexNumber(-2, -2)


def test_mul() -> None:
    assert ComplexNumber(2, 3) * ComplexNumber(4, -5) == ComplexNumber(23, 2)


def test_div() -> None:
    assert ComplexNumber(4, 2) / ComplexNumber(1, -1) == ComplexNumber(1.0, 3.0)


def test_conjugate() -> None:
    assert ComplexNumber(3, -4).conjugate() == ComplexNumber(3, 4)


def test_absolute() -> None:
    z = ComplexNumber(3, 4)
    assert z.abs_value() == 5


def test_expo() -> None:
    assert ComplexNumber(1, 1).exponentiation(1) == ComplexNumber(1, 1)
    # potência 1 = ele mesmo né
