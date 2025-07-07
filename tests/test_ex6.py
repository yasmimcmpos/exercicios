from exercicios.ex6 import maior_palindromo, se_e_palindromo


def test__se_e_palindromo():
    assert se_e_palindromo(121)
    assert se_e_palindromo(12321)
    # assert se_e_palindromo(12345)
    assert not se_e_palindromo(12345)


def test_maior_palindromo_exemplo():
    assert maior_palindromo(2) == 9009


def test_maior_palindromo():
    assert maior_palindromo(3) == 906609
