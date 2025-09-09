from exercicios.ex16 import PositionPrimeNumber


def test_position() -> None:
    assert PositionPrimeNumber(10_001) == 104_743
