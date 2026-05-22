# Visual Design Notes

This project is designed as a visual path-planning comparison tool.

The main goal is to show how different search algorithms explore a grid map step by step.

## Cell States

The grid will use visual states for:

- free cells
- obstacle cells
- start cell
- goal cell
- frontier / open-set cells
- visited cells
- current cell
- final path cells

## Planned Algorithm Visualization

Each algorithm should expose its search process as a sequence of steps.

At each step, the visualizer should be able to show:

- which cell is currently being expanded
- which cells have already been visited
- which cells are in the frontier
- when the goal is found
- the final reconstructed path

## Planned Comparison

The project should compare algorithms using both visual and numeric outputs:

- final path length
- number of visited cells
- number of frontier updates
- runtime
- success or failure
