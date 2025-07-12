from exercicios.ex7 import append, concatenate, filter, lenght, map


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
