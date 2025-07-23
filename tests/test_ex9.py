from exercicios.ex9 import mmc_in_list


def test_mmc_ex():
    num_ex = list(range(1, 11))
    result_ex = mmc_in_list(num_ex)
    assert result_ex == 2520


def test_mmc():
    num = list(range(1, 21))
    resultado = mmc_in_list(num)
    assert resultado == 232_792_560


# range para percorrer minha lista de 1 a 11 e 1 a 21
# Range: range(inicio, fim, passos)
