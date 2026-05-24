import os

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap

from search_algorithms import astar_weighted_search
from weighted_grid import build_demo_weighted_grid

FREE = 0
OBSTACLE = 1
START = 2
GOAL = 3
VISITED = 4
FRONTIER = 5
CURRENT = 6
PATH = 7
HIGH_COST = 8

COLOR_MAP = ListedColormap([
    "#ffffff",
    "#222222",
    "#2ecc71",
    "#e74c3c",
    "#85c1e9",
    "#f7dc6f",
    "#af7ac5",
    "#f06292",
    "#f5b041",
])


def build_visual_matrix(weighted_grid, step):
    grid = weighted_grid.grid

    matrix = [[FREE for _ in range(grid.cols)] for _ in range(grid.rows)]

    for row, col in grid.obstacles:
        matrix[row][col] = OBSTACLE

    for (row, col), cost in weighted_grid.costs.items():
        if cost > 1 and matrix[row][col] != OBSTACLE:
            matrix[row][col] = HIGH_COST

    for row, col in step.visited:
        if (row, col) not in [grid.start, grid.goal]:
            matrix[row][col] = VISITED

    for row, col in step.frontier:
        if (row, col) not in [grid.start, grid.goal]:
            matrix[row][col] = FRONTIER

    for row, col in step.path:
        if (row, col) not in [grid.start, grid.goal]:
            matrix[row][col] = PATH

    if step.current is not None and step.current not in [grid.start, grid.goal]:
        row, col = step.current
        matrix[row][col] = CURRENT

    sr, sc = grid.start
    gr, gc = grid.goal

    matrix[sr][sc] = START
    matrix[gr][gc] = GOAL

    return matrix


def add_legend(ax):
    legend_items = [
        plt.Line2D([0], [0], marker="s", color="w", label="Free cost=1", markerfacecolor="#ffffff", markeredgecolor="gray", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Obstacle", markerfacecolor="#222222", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="High cost=5", markerfacecolor="#f5b041", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Start", markerfacecolor="#2ecc71", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Goal", markerfacecolor="#e74c3c", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Visited", markerfacecolor="#85c1e9", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Frontier", markerfacecolor="#f7dc6f", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Current", markerfacecolor="#af7ac5", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Path", markerfacecolor="#f06292", markersize=10),
    ]

    ax.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.22, 1.0))


def draw_search_step(weighted_grid, step, output_path):
    grid = weighted_grid.grid
    matrix = build_visual_matrix(weighted_grid, step)

    fig, ax = plt.subplots(figsize=(10, 6))

    norm = BoundaryNorm(
        boundaries=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5],
        ncolors=COLOR_MAP.N,
    )

    ax.imshow(matrix, cmap=COLOR_MAP, norm=norm)

    ax.set_xticks(range(grid.cols))
    ax.set_yticks(range(grid.rows))
    ax.set_xticklabels(range(grid.cols))
    ax.set_yticklabels(range(grid.rows))

    ax.set_xticks([x - 0.5 for x in range(1, grid.cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, grid.rows)], minor=True)
    ax.grid(which="minor", color="lightgray", linestyle="-", linewidth=1)

    ax.set_title("Weighted A* Search Visualization")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    for spine in ax.spines.values():
        spine.set_visible(False)

    add_legend(ax)

    plt.tight_layout()
    os.makedirs("results", exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()


def path_cost(weighted_grid, path):
    if not path:
        return 0

    return sum(weighted_grid.cost(cell) for cell in path[1:])


def main():
    weighted_grid = build_demo_weighted_grid()
    steps = astar_weighted_search(weighted_grid)

    final_step = steps[-1]

    draw_search_step(
        weighted_grid=weighted_grid,
        step=final_step,
        output_path="results/weighted_astar_search_preview.png",
    )

    print("Saved: results/weighted_astar_search_preview.png")
    print(f"Search steps: {len(steps)}")
    print(f"Path found: {final_step.found}")
    print(f"Path length: {len(final_step.path)}")
    print(f"Path cost: {path_cost(weighted_grid, final_step.path)}")
    print(f"Visited cells: {len(final_step.visited)}")


if __name__ == "__main__":
    main()
