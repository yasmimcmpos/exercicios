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


def test_filter_e_par():
    assert filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_length():
    assert lenght([10, 20, 30, 40]) == 4


def test_map():
    assert list(map(lambda x: x * 2, [10, 2])) == [20, 4]


def test_foldl():
    assert foldl(lambda x, y: x + y, 0, [1, 3, 6, 8]) == 18


def test_foldl_exemplo2():
    assert foldl(lambda x, y: x + y, 1, [1, 3, 6, 8]) == 19
    # função, acumulador, lista


def test_foldr():
    assert foldr(lambda x, y: x - y, 0, [1, 2, 6]) == 5
    # Explicando subtraicao(1, subtracao(2, subtracao(6, 0)) -->
    # subtracao(1, subtracao(2,6) -->
    # subtracao(1,-4) --> 5


def test_reverse():
    assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
