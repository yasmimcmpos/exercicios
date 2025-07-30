from exercicios.ex11 import square_of_the_sum, sum_of_the_square


def test_difference() -> None:
    assert square_of_the_sum() - sum_of_the_square() == 25_164_150
