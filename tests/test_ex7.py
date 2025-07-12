from exercicios.ex7 import (
    append,
    concatenate,
    filter,
    foldl,
    foldr,
    lenght,
    map,
    reverse,
)


def test_append():
    assert append([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concatenate():
    assert concatenate([[1, 2], [], [3, 6]]) == [1, 2, 3, 6]


def e_par(x):
    return x % 2 == 0


def test_filter_e_par():
    assert filter(e_par, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_length():
    assert lenght([10, 20, 30, 40]) == 4


def dobrar(x):
    return x * 2


def test_map():
    assert map(dobrar, [10, 2]) == [20, 4]


def soma(x, y):
    return x + y


def test_foldl():
    assert foldl(soma, 0, [1, 3, 6, 8]) == 18


def test_foldl_exemplo2():
    assert foldl(soma, 1, [1, 3, 6, 8]) == 19
    # função, acumulador, lista


def subtracao(x, y):
    return x - y


def test_foldr():
    assert foldr(subtracao, 0, [1, 2, 6]) == 5
    # Explicando subtraicao(1, subtracao(2, subtracao(6, 0)) -->
    # subtracao(1, subtracao(2,6) -->
    # subtracao(1,-4) --> 5


def test_reverse():
    assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
