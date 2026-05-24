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


def dijkstra_search(grid: GridMap) -> List[SearchStep]:
    import heapq

    heap = [(0, grid.start)]
    visited = set()
    parent = {grid.start: None}
    distance = {grid.start: 0}

    steps = [
        SearchStep(
            current=grid.start,
            visited=set(),
            frontier={grid.start},
            path=[],
            found=False,
        )
    ]

    while heap:
        current_distance, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == grid.goal:
            path = rebuild_path(parent, grid.goal)
            steps.append(
                SearchStep(
                    current=current,
                    visited=set(visited),
                    frontier=set(cell for _, cell in heap if cell not in visited),
                    path=path,
                    found=True,
                )
            )
            return steps

        for neighbor in get_neighbors(current, grid):
            new_distance = current_distance + 1

            if neighbor not in distance or new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current
                heapq.heappush(heap, (new_distance, neighbor))

        steps.append(
            SearchStep(
                current=current,
                visited=set(visited),
                frontier=set(cell for _, cell in heap if cell not in visited),
                path=[],
                found=False,
            )
        )

    steps.append(
        SearchStep(
            current=None,
            visited=set(visited),
            frontier=set(),
            path=[],
            found=False,
        )
    )

    return steps


def dijkstra_weighted_search(weighted_grid) -> List[SearchStep]:
    import heapq

    grid = weighted_grid.grid

    heap = [(0, grid.start)]
    visited = set()
    parent = {grid.start: None}
    distance = {grid.start: 0}

    steps = [
        SearchStep(
            current=grid.start,
            visited=set(),
            frontier={grid.start},
            path=[],
            found=False,
        )
    ]

    while heap:
        current_distance, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == grid.goal:
            path = rebuild_path(parent, grid.goal)
            steps.append(
                SearchStep(
                    current=current,
                    visited=set(visited),
                    frontier=set(cell for _, cell in heap if cell not in visited),
                    path=path,
                    found=True,
                )
            )
            return steps

        for neighbor in get_neighbors(current, grid):
            new_distance = current_distance + weighted_grid.cost(neighbor)

            if neighbor not in distance or new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current
                heapq.heappush(heap, (new_distance, neighbor))

        steps.append(
            SearchStep(
                current=current,
                visited=set(visited),
                frontier=set(cell for _, cell in heap if cell not in visited),
                path=[],
                found=False,
            )
        )

    steps.append(
        SearchStep(
            current=None,
            visited=set(visited),
            frontier=set(),
            path=[],
            found=False,
        )
    )

    return steps


def manhattan_distance(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(grid: GridMap) -> List[SearchStep]:
    import heapq

    heap = [(0, grid.start)]
    visited = set()
    parent = {grid.start: None}

    steps = [
        SearchStep(
            current=grid.start,
            visited=set(),
            frontier={grid.start},
            path=[],
            found=False,
        )
    ]

    while heap:
        _, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == grid.goal:
            path = rebuild_path(parent, grid.goal)

            steps.append(
                SearchStep(
                    current=current,
                    visited=set(visited),
                    frontier=set(cell for _, cell in heap if cell not in visited),
                    path=path,
                    found=True,
                )
            )

            return steps

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                parent[neighbor] = current

                heuristic = manhattan_distance(neighbor, grid.goal)

                heapq.heappush(heap, (heuristic, neighbor))

        steps.append(
            SearchStep(
                current=current,
                visited=set(visited),
                frontier=set(cell for _, cell in heap if cell not in visited),
                path=[],
                found=False,
            )
        )

    steps.append(
        SearchStep(
            current=None,
            visited=set(visited),
            frontier=set(),
            path=[],
            found=False,
        )
    )

    return steps
