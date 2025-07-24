from exercicios.ex8_class import SpaceAge


def test_space_age():
    pessoa = SpaceAge(1_000_000_000)
    assert round(pessoa.age_on("mercury"), 2) == 131.57
    assert round(pessoa.age_on("venus"), 2) == 51.51
    assert round(pessoa.age_on("earth"), 2) == 31.69
    assert round(pessoa.age_on("mars"), 2) == 16.85
    assert round(pessoa.age_on("jupiter"), 2) == 2.67
    assert round(pessoa.age_on("saturn"), 2) == 1.08
    assert round(pessoa.age_on("uranus"), 2) == 0.38
    assert round(pessoa.age_on("neptune"), 2) == 0.19
    print("✨ All tests passed!")
