from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from grid_map import Cell, GridMap


@dataclass
class SearchStep:
    current: Optional[Cell]
    visited: Set[Cell]
    frontier: Set[Cell]
    path: List[Cell]
    found: bool


def get_neighbors(cell: Cell, grid: GridMap) -> List[Cell]:
    row, col = cell

    candidates = [
        (row - 1, col),
        (row, col + 1),
        (row + 1, col),
        (row, col - 1),
    ]

    obstacle_set = set(grid.obstacles)
    neighbors = []

    for nr, nc in candidates:
        inside_grid = 0 <= nr < grid.rows and 0 <= nc < grid.cols
        if inside_grid and (nr, nc) not in obstacle_set:
            neighbors.append((nr, nc))

    return neighbors


def rebuild_path(parent: Dict[Cell, Optional[Cell]], goal: Cell) -> List[Cell]:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def bfs_search(grid: GridMap) -> List[SearchStep]:
    queue = deque([grid.start])
    visited = {grid.start}
    parent = {grid.start: None}

    steps = [
        SearchStep(
            current=grid.start,
            visited=set(visited),
            frontier=set(queue),
            path=[],
            found=False,
        )
    ]

    while queue:
        current = queue.popleft()

        if current == grid.goal:
            path = rebuild_path(parent, grid.goal)
            steps.append(
                SearchStep(
                    current=current,
                    visited=set(visited),
                    frontier=set(queue),
                    path=path,
                    found=True,
                )
            )
            return steps

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

        steps.append(
            SearchStep(
                current=current,
                visited=set(visited),
                frontier=set(queue),
                path=[],
                found=False,
            )
        )

    steps.append(
        SearchStep(
            current=None,
            visited=set(visited),
            frontier=set(queue),
            path=[],
            found=False,
        )
    )

    return steps
