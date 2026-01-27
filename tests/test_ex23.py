import exercicios.ex23 from convert....

def test_convert_phrases():
    assert convert("As Soon As Possible") == "ASAP"
    assert convert("Liquid-crystal display") == "LCP"
    assert convert("Thank George it's Friday!") == "TGIF"
    assert convert("Portable Network   Graphics") == "PNG"