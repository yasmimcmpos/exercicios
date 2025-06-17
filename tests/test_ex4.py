import pytest


def test_diferenca_quadrados() -> None:

    assert diferenca_quadrados(10) == 2640
    assert diferenca_quadrados(5) == 170
    assert diferenca_quadrados(20) == 41230
