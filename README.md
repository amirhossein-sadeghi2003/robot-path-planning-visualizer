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

### Dijkstra Search Result

![Dijkstra Search Preview](results/dijkstra_search_preview.png)

### Dijkstra Search Animation

![Dijkstra Search Animation](results/dijkstra_search.gif)

## Current Status

The project currently includes:

- a demo grid map with obstacles, start, and goal cells
- Breadth-First Search implementation
- Dijkstra Search implementation
- search-state tracking for both algorithms
- static visualization of the final BFS search result
- static visualization of the final Dijkstra search result
- animated GIF showing the BFS exploration process
- animated GIF showing the Dijkstra exploration process
- path reconstruction visualization after the goal is found

## Implemented Algorithms

### Breadth-First Search

BFS explores the grid level by level from the start cell. In this project, each search step records:

- the current cell being expanded
- visited cells
- frontier cells
- the final reconstructed path
- whether the goal has been found

### Dijkstra Search

Dijkstra explores the grid based on the current shortest known path cost. In the current uniform-cost grid, its final path can look similar to BFS, but it provides the foundation for future weighted-grid experiments.

Each search step records:

- the current cell being expanded
- visited cells
- frontier cells
- the final reconstructed path
- whether the goal has been found

## Planned Algorithms

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
│   ├── bfs_search.gif
│   ├── dijkstra_search_preview.png
│   └── dijkstra_search.gif
├── src/
│   ├── grid_map.py
│   ├── preview_grid.py
│   ├── search_algorithms.py
│   ├── run_bfs_demo.py
│   ├── run_bfs_animation.py
│   ├── run_dijkstra_demo.py
│   └── run_dijkstra_animation.py
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

Generate the Dijkstra static visualization:

python src/run_dijkstra_demo.py

Generate the Dijkstra animation:

python src/run_dijkstra_animation.py
