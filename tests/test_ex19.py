from time import time

import pytest

from exercicios.ex19 import fatores_primos


def test_fatores_primos_basicos() -> None:
    assert fatores_primos(2) == [2]
    assert fatores_primos(3) == [3]
    assert fatores_primos(4) == [2, 2]
    assert fatores_primos(6) == [2, 3]
    assert fatores_primos(12) == [2, 2, 3]
    assert fatores_primos(37) == [37]
    assert fatores_primos(100) == [2, 2, 5, 5]


def test_fatores_primos_numero_grande() -> None:
    n = 1_000_003 * 1_000_033
    inicio = time()
    fatores = fatores_primos(n)
    duracao = time() - inicio

    assert fatores == [1_000_003, 1_000_033]
    assert duracao < 1.0, f"Muito lento: {duracao:.4f}s"


def test_fatores_primos_valor_invalido() -> None:
    with pytest.raises(ValueError):
        fatores_primos(1)
    with pytest.raises(ValueError):
        fatores_primos(0)
    with pytest.raises(ValueError):
        fatores_primos(-5)


def test_fatores_primos_com_numero_com_muitos_divisores() -> None:
    n = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    fatores = fatores_primos(n)
    assert fatores == [2, 3, 5, 7, 11, 13, 17, 19]
