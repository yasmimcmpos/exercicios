import pytest

from exercicios.ex15 import PigLatin


@pytest.mark.parametrize(
    "word, piglatin",
    [
        ("apple", "appleay"),
        ("xray", "xrayay"),
    ],
)
def test_word_beginning_vowel(word: str, piglatin: str) -> None:
    assert PigLatin(word).translate_word() == piglatin

    # assert PigLatin("xray").translate_word() == "xrayay"
    # assert PigLatin("yttria").translate_word() == "yttriaay"
    # assert PigLatin("pig").translate_word() == "igpay"
    # assert PigLatin("chair").translate_word() == "airchay"
    # assert PigLatin("thrush").translate_word() == "ushthray"
    # assert PigLatin("quick").translate_word() == "ickquay"
    # assert PigLatin("square").translate_word() == "aresquay"
    # assert PigLatin("my").translate_word() == "ymay"
    # assert PigLatin("rhythm").translate_word() == "ythmrhay"
    # assert PigLatin("object").translate_word() == "objectay"
    # assert PigLatin("under").translate_word() == "underay"
    # assert PigLatin("equal").translate_word() == "equalay"
    # assert PigLatin("liquid").translate_word() == "iquidlay"
    # assert PigLatin("school").translate_word() == "oolschay"
    # assert PigLatin("yellow").translate_word() == "ellowyay"
    # assert PigLatin("yttria").translate_word() == "yttriaay"
    # assert PigLatin("therapy").translate_word() == "erapythay"
    # assert PigLatin("queen").translate_word() == "eenquay"
    # assert PigLatin("xenon").translate_word() == "enonxay"
    # assert PigLatin("koala").translate_word() == "oalakay"
    # assert PigLatin("igloo").translate_word() == "iglooay"
    # assert PigLatin("igloo").translate_word() == "iglooay"
    # assert PigLatin("igloo").translate_word() == "iglooay"
    # assert PigLatin("igloo").translate_word() == "iglooay"
