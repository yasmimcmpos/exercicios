from exercicios.ex8 import SpaceAge


def test_calc_year_on_planet():
    """
    Observations: round(...,2)
    - '2' how many decimal places to keep at the end
    """
    year = 1_000_000_000
    assert round(SpaceAge(year, "mercury"), 2) == 131.57, "mercury failure"
    assert round(SpaceAge(year, "venus"), 2) == 51.51, "venus failure"
    assert round(SpaceAge(year, "mars"), 2) == 16.85, "mars failure"
    assert round(SpaceAge(year, "jupiter"), 2) == 2.67, "jupiter failure"
    assert round(SpaceAge(year, "saturn"), 2) == 1.08, "saturn failure"
    assert round(SpaceAge(year, "uranus"), 2) == 0.38, "uranus failure"
    assert round(SpaceAge(year, "neptune"), 2) == 0.19, "neptune failure"
