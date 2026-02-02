from exercicios.ex22 import find_greatest_product, load_grid
from os.path import join

def test_find_max_prod() -> None:
    test_dir = Path(__file__).resolve()
    project_dir = test_dir.parent
    filename = join(project_dir, "data", "grid.csv")
    grid = load_grid(filename)
    result, group, direction = find_greatest_product(grid)

    assert result == 70_600_674
    assert set(group) == {87, 97, 94, 89}
    assert direction in {"↘", "↙"}
