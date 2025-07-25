from exercicios.ex9 import mmc_in_list


def test_mmc_ex() -> None:
    assert mmc_in_list(list(range(1, 11))) == 2520


def test_mmc() -> None:
    assert mmc_in_list(list(range(1, 21))) == 232_792_560


# Range: range(inicio, fim, passos)
