import pytest

from exercicios.ex16 import find_prime_at_position


@pytest.mark.parametrize(
    "position, expected",
    [
        (1, 2),  # 1º primo
        (6, 13),  # 6º primo
        (10, 29),  # 10º primo
        (10_001, 104_743),  # 10.001º primo
    ],
)
def test_find_prime_at_position(position: int, expected: int) -> None:
    # Teste se find_prime_at_position retorna o número primo correto em
    # uma posição
    assert find_prime_at_position(position) == expected


# OU


def test_position() -> None:
    assert find_prime_at_position(10_001) == 104_743
