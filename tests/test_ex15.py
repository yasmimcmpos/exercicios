from exercicios.ex15 import PigLatin


def test_word_beginning_vowel() -> None:
    pig = PigLatin()
    assert pig.translate_word("apple") == "appleay"
    assert pig.translate_word("xray") == "xrayay"
    assert pig.translate_word("yttria") == "yttriaay"
    assert pig.translate_word("pig") == "igpay"
    assert pig.translate_word("chair") == "airchay"
    assert pig.translate_word("thrush") == "ushthray"
    assert pig.translate_word("quick") == "ickquay"
    assert pig.translate_word("square") == "aresquay"
    assert pig.translate_word("my") == "ymay"
    assert pig.translate_word("rhythm") == "ythmrhay"
    assert pig.translate_word("object") == "objectay"
    assert pig.translate_word("under") == "underay"
    assert pig.translate_word("equal") == "equalay"
    assert pig.translate_word("liquid") == "iquidlay"
    assert pig.translate_word("school") == "oolschay"
    assert pig.translate_word("yellow") == "ellowyay"
    assert pig.translate_word("yttria") == "yttriaay"
    assert pig.translate_word("therapy") == "erapythay"
    assert pig.translate_word("queen") == "eenquay"
    assert pig.translate_word("xenon") == "enonxay"
    assert pig.translate_word("koala") == "oalakay"
    assert pig.translate_word("igloo") == "iglooay"
