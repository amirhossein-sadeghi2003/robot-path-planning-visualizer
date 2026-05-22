from dataclasses import dataclass
from typing import List, Tuple

Cell = Tuple[int, int]

FREE = 0
OBSTACLE = 1
START = 2
GOAL = 3


@dataclass
class GridMap:
    rows: int
    cols: int
    start: Cell
    goal: Cell
    obstacles: List[Cell]

    def to_matrix(self):
        grid = [[FREE for _ in range(self.cols)] for _ in range(self.rows)]

        for r, c in self.obstacles:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                grid[r][c] = OBSTACLE

        sr, sc = self.start
        gr, gc = self.goal

        grid[sr][sc] = START
        grid[gr][gc] = GOAL

        return grid


def build_demo_grid():
    rows = 12
    cols = 16

    start = (1, 1)
    goal = (10, 13)

    obstacles = [
        (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
        (6, 5), (8, 5), (9, 5), (10, 5),

        (3, 8), (3, 9), (3, 10), (3, 11),
        (7, 8), (7, 9), (7, 10), (7, 11),

        (5, 2), (5, 3), (5, 4),
        (8, 10), (9, 10), (10, 10),

        (2, 13), (3, 13), (4, 13), (5, 13),
    ]

    return GridMap(
        rows=rows,
        cols=cols,
        start=start,
        goal=goal,
        obstacles=obstacles,
    )
