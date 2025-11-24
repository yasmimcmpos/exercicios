from exercicios.ex21 import say


def test_zero() -> None:
    assert say(0) == "zero"


def test_one() -> None:
    assert say(1) == "one"


def test_fourteen() -> None:
    assert say(14) == "fourteen"


def test_twenty() -> None:
    assert say(20) == "twenty"


def test_twenty_two() -> None:
    assert say(22) == "twenty-two"


def test_thirty() -> None:
    assert say(30) == "thirty"


def test_ninety_nine() -> None:
    assert say(99) == "ninety-nine"


def test_one_hundred() -> None:
    assert say(100) == "one hundred"


def test_one_hundred_twenty_three() -> None:
    assert say(123) == "one hundred twenty-three"


def test_two_hundred() -> None:
    assert say(200) == "two hundred"


def test_nine_hundred_ninety_nine() -> None:
    assert say(999) == "nine hundred ninety-nine"


def test_one_thousand() -> None:
    assert say(1000) == "one thousand"


def test_one_thousand_two_hundred_thirty_four() -> None:
    assert say(1234) == "one thousand two hundred thirty-four"


def test_one_million() -> None:
    assert say(1_000_000) == "one million"


def test_one_million_two_thousand_three_hundred_forty_five() -> None:
    assert say(1_002_345) == "one million two thousand three hundred forty-five"


def test_one_billion() -> None:
    assert say(1_000_000_000) == "one billion"


def test_a_big_number() -> None:
    assert (
        say(987_654_321_123)
        == "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three"
    )


def test_one_hundred_seventy() -> None:
    assert say(170) == "one hundred seventy"
    assert say(170) == "one hundred seventy"
