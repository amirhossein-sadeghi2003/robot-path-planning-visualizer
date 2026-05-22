import os

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap

from grid_map import build_demo_grid

COLOR_MAP = ListedColormap([
    "#ffffff",
    "#222222",
    "#2ecc71",
    "#e74c3c",
])

LABELS = {
    0: "Free",
    1: "Obstacle",
    2: "Start",
    3: "Goal",
}


def draw_grid(matrix, output_path, title):
    rows = len(matrix)
    cols = len(matrix[0])

    fig, ax = plt.subplots(figsize=(10, 6))

    norm = BoundaryNorm(
        boundaries=[-0.5, 0.5, 1.5, 2.5, 3.5],
        ncolors=COLOR_MAP.N,
    )

    ax.imshow(matrix, cmap=COLOR_MAP, norm=norm)

    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows))

    ax.set_xticks([x - 0.5 for x in range(1, cols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, rows)], minor=True)
    ax.grid(which="minor", color="lightgray", linestyle="-", linewidth=1)

    ax.set_title(title)
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    for spine in ax.spines.values():
        spine.set_visible(False)

    legend_items = [
        plt.Line2D([0], [0], marker="s", color="w", label="Free", markerfacecolor="#ffffff", markeredgecolor="gray", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Obstacle", markerfacecolor="#222222", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Start", markerfacecolor="#2ecc71", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Goal", markerfacecolor="#e74c3c", markersize=10),
    ]

    ax.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.18, 1.0))

    plt.tight_layout()
    os.makedirs("results", exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()


def main():
    grid = build_demo_grid()
    matrix = grid.to_matrix()

    draw_grid(
        matrix,
        output_path="results/grid_preview.png",
        title="Grid Map Preview",
    )

    print("Saved: results/grid_preview.png")


if __name__ == "__main__":
    main()
