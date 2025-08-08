from exercicios.ex12 import cesar


def test_cesar() -> None:
    key = 3
    assert cesar("Y", key) == "B"


# def test_cesar_frase() -> None:
#     key = 3
#     assert cesar("Hello World!", key) == "Khoor Zruog!"
