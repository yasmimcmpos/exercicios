from exercicios.ex22 import find_greatest_product, load_grid

EXPECTED = 70600674


def test_find_max_prod() -> None:
    grid = load_grid("grid.csv")
    result, group, direction = find_greatest_product(grid)

    assert result == 70600674
    assert set(group) == {87, 97, 94, 89}
    assert direction in {"↘", "↙"}
