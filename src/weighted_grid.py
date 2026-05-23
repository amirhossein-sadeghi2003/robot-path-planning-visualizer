from dataclasses import dataclass
from typing import Dict

from grid_map import Cell, GridMap, build_demo_grid


@dataclass
class WeightedGrid:
    grid: GridMap
    costs: Dict[Cell, int]

    def cost(self, cell: Cell) -> int:
        return self.costs.get(cell, 1)


def build_demo_weighted_grid():
    grid = build_demo_grid()

    costs = {}

    rough_cells = [
        (1, 9), (1, 10), (1, 11), (1, 12),
        (2, 9), (2, 10), (2, 11), (2, 12),
        (4, 8), (4, 9), (4, 10), (4, 11),
        (5, 8), (5, 9), (5, 10), (5, 11),
        (8, 7), (8, 8), (8, 9),
        (9, 7), (9, 8), (9, 9),
    ]

    for cell in rough_cells:
        costs[cell] = 5

    return WeightedGrid(grid=grid, costs=costs)
