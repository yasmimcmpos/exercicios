from exercicios.ex5 import maior_fator_primo


def test_maior_fator_primo_ex():  ##TODO ex6 fazer caso de ex primeiro
    assert maior_fator_primo(13_195) == 29


def test_maior_fator_primo():
    assert maior_fator_primo(6_00_851_475_143) == 6857


# ERRO: assert maior_fator_primo(6_008_514_751_413) == 6_857
