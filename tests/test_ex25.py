from exercicios.ex25 import slices


def test_slices_of_one_from_one() -> None:
    assert slices("1", 1) == ["1"]


def test_slices_of_one_from_two() -> None:
    assert slices("12", 1) == ["1", "2"]


def test_slices_of_two() -> None:
    assert slices("35", 2) == ["35"]


def test_slices_of_two_overlap() -> None:
    assert slices("9142", 2) == ["91", "14", "42"]


def test_slices_can_include_duplicates() -> None:
    assert slices("777777", 3) == ["777", "777", "777", "777"]


def test_slices_of_a_long_series() -> None:
    assert slices("918493904243", 5) == [
        "91849",
        "18493",
        "84939",
        "49390",
        "93904",
        "39042",
        "90424",
        "04243",
    ]


def test_slice_length_is_too_large() -> None:
    with raises(ValueError) as err:
        slices("12345", 6)
    assert str(err.value) == "slice length cannot be greater than series length"


def test_slice_length_is_way_too_large() -> None:
    with raises(ValueError) as err:
        slices("12345", 42)
    assert str(err.value) == "slice length cannot be greater than series length"


def test_slice_length_cannot_be_zero() -> None:
    with raises(ValueError) as err:
        slices("12345", 0)
    assert str(err.value) == "slice length cannot be zero"


def test_slice_length_cannot_be_negative() -> None:
    with raises(ValueError) as err:
        slices("123", -1)
    assert str(err.value) == "slice length cannot be negative"


def test_empty_series_is_invalid() -> None:
    with raises(ValueError) as err:
        slices("", 1)
    assert str(err.value) == "series cannot be empty"
