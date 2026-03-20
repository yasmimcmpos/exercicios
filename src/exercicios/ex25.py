# https://exercism.org/tracks/python/exercises/series


def slices(series: str, length: int) -> list[str]:
    if series == "":
        raise ValueError("series cannot be empty")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result: list[str] = []

    for i in range(len(series) - length + 1):
        result.append(series[i : i + length])

    return result
