from exercicios.ex15 import PigLatin


def test_word_beginning_vowel() -> None:
    pig = PigLatin()
    assert pig.translate_word("apple") == "appleay"
    assert pig.translate_word("xray") == "xrayay"
