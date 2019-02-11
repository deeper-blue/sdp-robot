# High Level Interface
Description of the high-level interface.

Public state:

- `board_state`: the current state of the board. Would be stored as array of cells and contain which piece is in which cell.

### `take_piece_from(cellA, cellB)`
Take the current piece at cellA and move it to cellB.
Would call the respective LLI functions to perform movement. Only used when moving a piece to empty cell.

**Assumptions**:

- The physical robot is in its preset state (i.e. arch centered, etc).

**Effects**:

- Piece X is moved from cellA to cellB on the physical board.
- Board state is updated

### `replace_piece_at(cellA, cellB)`
Replaces the current piece at cellA with the one at cellB.
Would call the respective LLI functions to perform movement. Only used when taking another piece.

**Assumptions**:

- The physical robot is in its preset state (i.e. arch centered, etc).

**Effects**:

- Piece X is moved from cell to the buffer on the physical board.
- Board state is updated

### `take_piece_in(cell)`
Take the current piece at cell and move it to buffer.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- The physical robot is in its preset state (i.e. arch centered, etc).

**Effects**:

- Piece X is moved from cell to the buffer on the physical board.
- Board state is updated

### `reset()`
Resets the robot.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- *None*

**Effects**:

- Robot is set to preset state.

### `perform_castling_at(cellA, cellB)`
Performs the castling move on the pieces at cellA and cellB.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- The pieces are able and allowed to perform the castling move

**Effects**:

- Castling move is performed.
- Board state updated

### `check_board_state()`
Checks the current state of the board
Would call the respective LLI functions to perform movement.

**Assumptions**:

- *None*

**Effects**:

- Board state is checked

## Notes
- Is the buffer represented as cells?
- Board state may need more thought, would we need to store it as the state of each piece or for example only store it as each cell being empty and non empty?
- check_board_state possibly useless function?
