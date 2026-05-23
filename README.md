# Robot Path Planning Visualizer

A visual robotics-oriented path planning project that shows how search algorithms explore a grid map and find a path from a start cell to a goal cell.

The main goal is not only to compute the final path, but also to make the search process visible step by step.

## Demo

### Grid Map

![Grid Preview](results/grid_preview.png)

### Weighted Grid Cost Map

![Weighted Grid Preview](results/weighted_grid_preview.png)

### BFS Search Result

![BFS Search Preview](results/bfs_search_preview.png)

### BFS Search Animation

![BFS Search Animation](results/bfs_search.gif)

### Dijkstra Search Result

![Dijkstra Search Preview](results/dijkstra_search_preview.png)

### Dijkstra Search Animation

![Dijkstra Search Animation](results/dijkstra_search.gif)

### Weighted Dijkstra Search Result

![Weighted Dijkstra Search Preview](results/weighted_dijkstra_search_preview.png)

### Weighted Dijkstra Search Animation

![Weighted Dijkstra Search Animation](results/weighted_dijkstra_search.gif)

## Current Status

The project currently includes:

- a demo grid map with obstacles, start, and goal cells
- a weighted grid cost map
- Breadth-First Search implementation
- Dijkstra Search implementation
- weighted Dijkstra Search implementation
- search-state tracking for implemented algorithms
- static visualizations of search results
- animated GIFs showing the exploration process
- path reconstruction visualization after the goal is found

## Implemented Algorithms

### Breadth-First Search

BFS explores the grid level by level from the start cell. In this project, each search step records:

- the current cell being expanded
- visited cells
- frontier cells
- the final reconstructed path
- whether the goal has been found

BFS treats every valid move as having the same cost.

### Dijkstra Search

Dijkstra explores the grid based on the current shortest known path cost.

On a uniform-cost grid, its final path can look similar to BFS. On a weighted grid, Dijkstra can prefer a longer path with lower total cost instead of the shortest path in number of steps.

Each search step records:

- the current cell being expanded
- visited cells
- frontier cells
- the final reconstructed path
- whether the goal has been found

### Weighted Dijkstra Search

The weighted version uses a cost map where some cells are more expensive to cross.

This makes the difference between shortest path and lowest-cost path more visible.

## Planned Algorithms

- Greedy Best-First Search
- A* Search

## Visual Features

The visualizer uses different cell states for:

- free cells
- obstacle cells
- high-cost cells
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
│   ├── weighted_grid_preview.png
│   ├── bfs_search_preview.png
│   ├── bfs_search.gif
│   ├── dijkstra_search_preview.png
│   ├── dijkstra_search.gif
│   ├── weighted_dijkstra_search_preview.png
│   └── weighted_dijkstra_search.gif
├── src/
│   ├── grid_map.py
│   ├── weighted_grid.py
│   ├── preview_grid.py
│   ├── preview_weighted_grid.py
│   ├── search_algorithms.py
│   ├── run_bfs_demo.py
│   ├── run_bfs_animation.py
│   ├── run_dijkstra_demo.py
│   ├── run_dijkstra_animation.py
│   ├── run_weighted_dijkstra_demo.py
│   └── run_weighted_dijkstra_animation.py
├── .gitignore
├── README.md
└── requirements.txt

## How to Run

Create or activate a Python virtual environment, then install the required packages:

pip install -r requirements.txt

Generate the initial grid preview:

python src/preview_grid.py

Generate the weighted grid preview:

python src/preview_weighted_grid.py

Generate the BFS static visualization:

python src/run_bfs_demo.py

Generate the BFS animation:

python src/run_bfs_animation.py

Generate the Dijkstra static visualization:

python src/run_dijkstra_demo.py

Generate the Dijkstra animation:

python src/run_dijkstra_animation.py

Generate the weighted Dijkstra static visualization:

python src/run_weighted_dijkstra_demo.py

Generate the weighted Dijkstra animation:

python src/run_weighted_dijkstra_animation.py
