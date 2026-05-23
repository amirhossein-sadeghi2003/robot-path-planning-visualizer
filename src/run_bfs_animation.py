import os
import shutil
from copy import deepcopy
from pathlib import Path

import imageio.v2 as imageio
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm

from grid_map import build_demo_grid
from search_algorithms import SearchStep, bfs_search
from run_bfs_demo import COLOR_MAP, build_visual_matrix


def draw_frame(grid, step, output_path, frame_number, total_frames, phase_name):
    matrix = build_visual_matrix(grid, step)

    fig, ax = plt.subplots(figsize=(10, 6))

    norm = BoundaryNorm(
        boundaries=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5],
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

    title = f"BFS {phase_name} - Frame {frame_number}/{total_frames}"
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
        plt.Line2D([0], [0], marker="s", color="w", label="Visited", markerfacecolor="#85c1e9", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Frontier", markerfacecolor="#f7dc6f", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Current", markerfacecolor="#af7ac5", markersize=10),
        plt.Line2D([0], [0], marker="s", color="w", label="Path", markerfacecolor="#f06292", markersize=10),
    ]

    ax.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.18, 1.0))

    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def select_search_steps(steps, stride=4):
    selected = steps[::stride]

    if selected[-1] != steps[-1]:
        selected.append(steps[-1])

    return selected


def build_path_reconstruction_steps(final_step):
    path_steps = []

    for i in range(1, len(final_step.path) + 1):
        partial_path = final_step.path[:i]

        step = SearchStep(
            current=final_step.path[i - 1],
            visited=set(final_step.visited),
            frontier=set(),
            path=partial_path,
            found=True,
        )

        path_steps.append(step)

    return path_steps


def main():
    grid = build_demo_grid()
    steps = bfs_search(grid)

    search_steps = select_search_steps(steps, stride=4)
    final_step = steps[-1]

    path_steps = build_path_reconstruction_steps(final_step)

    output_dir = Path("results")
    frame_dir = output_dir / "bfs_frames"

    os.makedirs(output_dir, exist_ok=True)

    if frame_dir.exists():
        shutil.rmtree(frame_dir)

    frame_dir.mkdir(parents=True)

    frame_paths = []

    combined_steps = []

    for step in search_steps:
        combined_steps.append((step, "Search Phase"))

    for step in path_steps:
        combined_steps.append((step, "Path Reconstruction Phase"))

    total_frames = len(combined_steps)

    for index, (step, phase_name) in enumerate(combined_steps, start=1):
        frame_path = frame_dir / f"frame_{index:03d}.png"
        draw_frame(
            grid=grid,
            step=step,
            output_path=frame_path,
            frame_number=index,
            total_frames=total_frames,
            phase_name=phase_name,
        )
        frame_paths.append(frame_path)

    images = [imageio.imread(frame_path) for frame_path in frame_paths]

    gif_path = output_dir / "bfs_search.gif"
    imageio.mimsave(gif_path, images, duration=0.18)

    shutil.rmtree(frame_dir)

    print(f"Saved: {gif_path}")
    print(f"Original search steps: {len(steps)}")
    print(f"Search frames: {len(search_steps)}")
    print(f"Path reconstruction frames: {len(path_steps)}")
    print(f"Total animation frames: {len(combined_steps)}")
    print(f"Path found: {final_step.found}")
    print(f"Path length: {len(final_step.path)}")
    print(f"Visited cells: {len(final_step.visited)}")


if __name__ == "__main__":
    main()
