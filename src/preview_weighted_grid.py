import os

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap

from grid_map import OBSTACLE, START, GOAL
from weighted_grid import build_demo_weighted_grid

FREE_LOW_COST = 0
OBSTACLE_CELL = 1
START_CELL = 2
GOAL_CELL = 3
HIGH_COST = 4

COLOR_MAP = ListedColormap([
    "#ffffff",
    "#222222",
    "#2ecc71",
    "#e74c3c",
    "#f5b041",
])


def build_cost_matrix(weighted_grid):
    grid = weighted_grid.grid
    matrix = [[FREE_LOW_COST for _ in range(grid.cols)] for _ in range(grid.rows)]

    for row, col in grid.obstacles:
        matrix[row][col] = OBSTACLE_CELL

    for (row, col), cost in weighted_grid.costs.items():
        if cost > 1 and matrix[row][col] != OBSTACLE_CELL:
            matrix[row][col] = HIGH_COST

    sr, sc = grid.start
    gr, gc = grid.goal

    matrix[sr][sc] = START_CELL
    matrix[gr][gc] = GOAL_CELL

    return matrix


def draw_weighted_grid(weighted_grid, output_path):
    grid = weighted_grid.grid
    matrix = build_cost_matrix(weighted_grid)

    fig, ax = plt.subplots(figsize=(10, 6))

    norm = BoundaryNorm(
        boundaries=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5],
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

    ax.set_title("Weighted Grid Preview")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    for spine in ax.spines.values():
        spine.set_visible(False)

    legend_items = [
        plt.Line2D([0], [0], marker="s", color="w", label="Free cost=1", markerfacecolor="#ffffff", markeredgecolor="gray", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Obstacle", markerfacecolor="#222222", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Start", markerfacecolor="#2ecc71", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Goal", markerfacecolor="#e74c3c", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="High cost=5", markerfacecolor="#f5b041", markersize=10),
    ]

    ax.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.22, 1.0))

    plt.tight_layout()
    os.makedirs("results", exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()


def main():
    weighted_grid = build_demo_weighted_grid()

    draw_weighted_grid(
        weighted_grid=weighted_grid,
        output_path="results/weighted_grid_preview.png",
    )

    print("Saved: results/weighted_grid_preview.png")
    print(f"High-cost cells: {len(weighted_grid.costs)}")


if __name__ == "__main__":
    main()
