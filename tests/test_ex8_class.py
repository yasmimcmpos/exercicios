from exercicios.ex8_class import SpaceAge


def test_space_age() -> None:
    pessoa = SpaceAge(1_000_000_000)

    assert round(pessoa.age_on_planet("mercury"), 2) == 131.57
    assert round(pessoa.age_on_planet("venus"), 2) == 51.51
    assert round(pessoa.age_on_planet("mars"), 2) == 16.85
    assert round(pessoa.age_on_planet("jupiter"), 2) == 2.67
    assert round(pessoa.age_on_planet("saturn"), 2) == 1.08
    assert round(pessoa.age_on_planet("uranus"), 2) == 0.38
    assert round(pessoa.age_on_planet("neptune"), 2) == 0.19
