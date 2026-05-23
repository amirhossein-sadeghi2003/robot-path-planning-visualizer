import os
import pandas as pd

from grid_map import build_demo_grid
from search_algorithms import bfs_search, dijkstra_search, dijkstra_weighted_search
from weighted_grid import build_demo_weighted_grid


def path_cost(weighted_grid, path):
    if not path:
        return 0

    return sum(weighted_grid.cost(cell) for cell in path[1:])


def summarize(name, steps, weighted_grid):
    final_step = steps[-1]

    return {
        "algorithm": name,
        "found": final_step.found,
        "path_length_cells": len(final_step.path),
        "weighted_path_cost": path_cost(weighted_grid, final_step.path),
        "visited_cells": len(final_step.visited),
        "search_steps": len(steps),
    }


def main():
    grid = build_demo_grid()
    weighted_grid = build_demo_weighted_grid()

    rows = [
        summarize("BFS", bfs_search(grid), weighted_grid),
        summarize("Dijkstra", dijkstra_search(grid), weighted_grid),
        summarize("Weighted Dijkstra", dijkstra_weighted_search(weighted_grid), weighted_grid),
    ]

    df = pd.DataFrame(rows)

    os.makedirs("results", exist_ok=True)
    output_path = "results/algorithm_comparison.csv"
    df.to_csv(output_path, index=False)

    print(df.to_string(index=False))
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
