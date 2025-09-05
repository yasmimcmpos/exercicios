import pytest

from exercicios.ex15 import PigLatin


@pytest.mark.parametrize(
    "word, piglatin",
    [
        ("apple", "appleay"),
        ("xray", "xrayay"),
        ("yttria", "yttriaay"),
        ("pig", "igpay"),
        ("chair", "airchay"),
        ("thrush", "ushthray"),
        ("quick", "ickquay"),
        ("square", "aresquay"),
        ("my", "ymay"),
        ("rhythm", "ythmrhay"),
        ("object", "objectay"),
        ("under", "underay"),
        ("liquid", "iquidlay"),
        ("school", "oolschay"),
        ("therapy", "erapythay"),
        ("queen", "eenquay"),
        ("xenon", "enonxay"),
        ("koala", "oalakay"),
        ("igloo", "iglooay"),
    ],
)
def test_word_beginning_vowel(word: str, piglatin: str) -> None:
    assert PigLatin(word).translate_word() == piglatin
