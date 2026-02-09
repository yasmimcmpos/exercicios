from exercicios.ex23 import convert


def test_convert_phrases() -> None:
    assert convert("As Soon As Possible") == "ASAP"
    assert convert("Liquid-crystal display") == "LCD"
    assert convert("Thank George it's Friday!") == "TGIF"
    assert convert("Portable Network   Graphics") == "PNG"
    assert convert("rock & roll") == "RR"
    assert convert("hello_world") == "H"
    assert convert("  Hello World  ") == "HW"
    assert convert("Complementary-metal-oxide semiconductor") == "CMOS"
    assert convert("!!! --- ???") == ""
