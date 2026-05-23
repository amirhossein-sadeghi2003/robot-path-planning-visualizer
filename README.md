# Robot Path Planning Visualizer

A visual robotics-oriented path planning project that shows how search algorithms explore a grid map and find a path from a start cell to a goal cell.

The main goal is not only to compute the final path, but also to make the search process visible step by step.

## Demo

### Grid Map

![Grid Preview](results/grid_preview.png)

### BFS Search Result

![BFS Search Preview](results/bfs_search_preview.png)

### BFS Search Animation

![BFS Search Animation](results/bfs_search.gif)

## Current Status

The project currently includes:

- a demo grid map with obstacles, start, and goal cells
- Breadth-First Search implementation
- BFS search-state tracking
- static visualization of the final BFS search result
- animated GIF showing the BFS exploration process
- path reconstruction visualization after the goal is found

## Implemented Algorithm

### Breadth-First Search

BFS explores the grid level by level from the start cell. In this project, each search step records:

- the current cell being expanded
- visited cells
- frontier cells
- the final reconstructed path
- whether the goal has been found

This makes it possible to visualize how the algorithm searches before it reaches the goal.

## Planned Algorithms

- Dijkstra Search
- Greedy Best-First Search
- A* Search

## Visual Features

The visualizer uses different cell states for:

- free cells
- obstacle cells
- start cell
- goal cell
- visited cells
- frontier cells
- current cell
- final path cells

## Portfolio Context

This project supports my broader portfolio direction in intelligent physical systems, robotics, and autonomous systems.

It complements projects in:

- sensor fusion and state estimation
- embedded sensing
- feedback control
- intelligent monitoring systems

In a robotics pipeline, state estimation helps a robot understand where it is, path planning helps it decide where to go, and control helps it follow the planned path.

## Repository Structure

robot-path-planning-visualizer/
├── docs/
├── results/
│   ├── grid_preview.png
│   ├── bfs_search_preview.png
│   └── bfs_search.gif
├── src/
│   ├── grid_map.py
│   ├── preview_grid.py
│   ├── search_algorithms.py
│   ├── run_bfs_demo.py
│   └── run_bfs_animation.py
├── .gitignore
├── README.md
└── requirements.txt

## How to Run

Create or activate a Python virtual environment, then install the required packages:

pip install -r requirements.txt

Generate the initial grid preview:

python src/preview_grid.py

Generate the BFS static visualization:

python src/run_bfs_demo.py

Generate the BFS animation:

python src/run_bfs_animation.py
