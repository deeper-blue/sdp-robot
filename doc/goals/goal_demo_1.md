# Demo 1 Goals

## Assumptions
Given:

- a static chess board,
- chess pieces that are after set-up only moved by the robot.

## Goals

### Necessary
Have:

- a basic frame from LEGO:
    - y-axis rails,
    - arch that moves along y-axis,
    - x-axis rails on the arch,
    - platform on the arch that moves along x-axis;
- a configuration file that keeps robot, board and environment details,
- a low-level interface to command the robot (e.g. `moveTo(cell)`, not the whole `movePiece(cellOrig, cellDest)`).

### Optimistic
Pontentially have:

- a grabber:
    - grabber descent and ascent mechanism on the platform,
    - grabber mechanism.
