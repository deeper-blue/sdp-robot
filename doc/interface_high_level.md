# High Level Interface
Description of the high-level interface.

Public state:

- `current_state`: the current state of the board stored as a cell
- `preset_state`: the preset state of the board stored as a cell

### `move(cellA, cellB, piece_type)`
Take the current piece at cellA and move it to cellB.
Would call the respective LLI functions to perform movement. Only used when moving a piece to empty cell.

**Assumptions**:

- The physical robot is in its preset state (i.e. arch centered, etc).

**Effects**:

- Piece X is moved from cellA to cellB on the physical board.
- Board state is updated

### `move_piece(cellA, cellB, piece_type)`
Moves the piece at cellA onto empty cellB, then go to preset state (reset).
Would call the respective LLI functions to perform movement. Only used when taking another piece.

**Assumptions**:

- cellB is empty

**Effects**:

- Piece X is moved from cell to the empty space on the physical board.
- Board state is updated

### `take_piece(cellA, cellB, piece, piece_type_A, piece_type_B)`
Take the current piece at cellB, move it to buffer, and replace it with piece at cellB. Then reset.
The piece is identified by its original position, which is used to compute its buffer position.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- The physical robot is in its preset state (i.e. arch centered, etc).
- There is an actual piece there
- `piece` is the original cell of the piece in `cellB`.

**Effects**:

- Piece X takes piece Y on board and moves to Y's cell. Y is placed in buffer.
- Board state is updated

### `reset()`
Resets the robot to the preset  position.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- Move has been completed

**Effects**:

- Robot is set to preset state.

### `perform_castling_at(cellA, cellB, cellC, cellD, piece_type_A, piece_type_B)`
Performs the castling move on the pieces at cellA and cellB and moves them to cells C and D respectively.
Would call the respective LLI functions to perform movement.

**Assumptions**:

- The pieces are able and allowed to perform the castling move

**Effects**:

- Castling move is performed.
- Board state updated

### `en_passant(cellA, cellB, cellTake, piece)`
Performs en passant, moving a piece from `cellA` to `cellB` and taking the piece with original position `piece` in `cellTake`.
The piece is identified by its original position, which is used to compute its buffer position.

**Assumption**:

- Robot is in preset state,
- `cellB` is empty,
- there are pawns in `cellA` and `cellTake`,
- `piece` is the original cell of the piece in `cellTake`.

**Effects**:

- Pawn in `cellA` is moved to `cellB`,
- pawn in `cellTake` is moved to the buffer cell based on supplied identifier,
- robot resets.


## Notes
- May still need to rework castling 
- `current_state` use is still not defined. Since we are always going to be in `preset_state` after a move.
