import pytest

from exercicios.ex18 import encontrar_trigemeo_pitagorico, verificar_trigemeo


@pytest.mark.parametrize(
    "total, expected_product",
    [
        (1_000, 31_875_000),
        (30, 780),
        (12, 60),
    ],
)
def test_encontrar_trigemeo_pitagorico(total: int, expected_product: int) -> None:
    result = encontrar_trigemeo_pitagorico(total)
    assert result is not None

    a, b, c = result

    assert a**2 + b**2 == c**2
    assert a + b + c == total
    assert a * b * c == expected_product


@pytest.mark.parametrize(
    "a, b, c",
    [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
    ],
)
def test_verificar_trigemeo_valido(a: int, b: int, c: int) -> None:
    assert verificar_trigemeo(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 2, 3),
        (2, 3, 4),
        (5, 6, 7),
    ],
)
def test_verificar_trigemeo_invalido(a: int, b: int, c: int) -> None:
    assert not verificar_trigemeo(a, b, c)
