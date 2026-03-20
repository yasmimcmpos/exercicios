# https://exercism.org/tracks/python/exercises/series


def slices(series: str, length: int) -> list[str]:
    """Generate all contiguous substrings of a given length from a digit series.

    Args:
        series (str): String containing the sequence of digits.
        length (int): Length of each slice.
    Raises:
        ValueError: If the series is empty.
        ValueError: If length is negative.
        ValueError: If length is zero.
        ValueError: If length is greater than the series length.

    Returns:
        list[str]: A list of substrings of size `length`
    """
    if series == "":
        raise ValueError("series cannot be empty")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i : i + length] for i in range(len(series) - length + 1)]
