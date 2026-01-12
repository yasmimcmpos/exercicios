# https://projecteuler.net/problem=11
# For the Grid.csv find the product of the four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in different directions.
# Qual é o maior produto de numeros adjacentes na mesma direção

import csv
from functools import reduce
from operator import mul
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_grid(filename: str | Path) -> list[list[int]]:
    """Lê um =arquivo CSV com números inteiros e o converte em uma matriz
    (lista de lista)

    Args:
        filename: Caminho do arquivo CSV.

    Returns:
        Matriz bidimensional de inteiros.
    """
    path = Path(filename)

    if not path.is_absolute():
        path = BASE_DIR / path

    grid: list[list[int]] = []

    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            grid.append([int(x) for x in row])

    return grid


def is_valid_start(rows: int, cols: int, row: int, col: int, dr: int, dc: int) -> bool:
    """Verifica se 4 posições cabem no grid a partir de uma coordenada e direção.

    Returns:
        bool: Confere se essa posição final ainda está dentro do grid.
    """
    end_row = row + dr * 3
    end_col = col + dc * 3

    return 0 <= end_row < rows and 0 <= end_col < cols


def get_group(grid: list[list[int]], row: int, col: int, dr: int, dc: int) -> list[int]:
    """Retorna os 4 números adjacentes a partir de uma posição e direção.

    Args:
        k : posição
        row (int): linha
        col (int):coluna
        dr (int): delta linha
        dc (int): delta coluna

    Obs.:
        (row,col) = return (Pegue o número que está k passos à frente,
        indo na direção (dr, dc) a partir de (row, col).”)
    """
    return [grid[row + dr * k][col + dc * k] for k in range(4)]


def find_greatest_product(grid: list[list[int]]) -> tuple[int, list[int], str]:
    """Encontra o maior produto de quatro números adjacentes no grid.

    Returns:
        tuple[int, list[int], str]: Entrega o resultado final.
    """
    rows = len(grid)
    cols = len(grid[0])

    max_product = 0
    best_group: list[int] = []
    best_direction: str = ""

    directions = {
        "→": (0, 1),
        "↓": (1, 0),
        "↘": (1, 1),
        "↙": (1, -1),
    }

    for row in range(rows):
        for col in range(cols):
            for name, (dr, dc) in directions.items():

                if not is_valid_start(rows, cols, row, col, dr, dc):
                    continue

                group = get_group(grid, row, col, dr, dc)
                product = reduce(mul, group, 1)

                if product > max_product:
                    max_product = product
                    best_group = group
                    best_direction = name

    return max_product, best_group, best_direction
