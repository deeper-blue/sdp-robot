# Low Level Interface
Description of the low-level interface.

## Arch
Public state:

- `position`: the position of the arch along the bottom rail in cm.
- `expected_error`: the expected error in cm, computed as `error = internal_position - real_position`.
    How much the arch would have to move to really be at internal position.

### `go_to_cell(cell)`
Moves the arch to be over a cell.
Computes the actual position to move to using cell size from the config, adjusting for the space between the board and buffer as needed.
If the expected error is over a preset threshold, first performs a position reset via `go_to_edge()` and then performs the movement.

**Assumptions**:

- The platform is in the centre (even load on motors).

**Effects**:

- If the expected error is over the threshold, performs a reset.
- The physical arch moves to have the grabber centred over the supplied cell column.
- Internal position is updated by the actual distance moved, with the result being "sufficiently close" to the centre of the desired cell column.
- Expected error is incremented by a factor of the actual distance moved.

### `go_to_edge()`
Moves the arch to the buffer side of the active area until the reset button is pressed.
On reset button press, stops the arch, sets internal position to the preconfigured edge position and resets expected error to zero.

**Assumptions**:

- The platform is in the centre (even load on motors).

**Effects**:

- The physical arch moves to the buffer-side edge of the active area.
- Internal position is set to preconfigured edge position.
- Expected error is set to zero.

## Platform
Public state:

- `position`: the position of the platform along the top rail in cm.
- `expected_error`: the expected error in cm, computed as `error = internal_position - real_position`.
    How much the platform would have to move to really be at internal position.

### `go_to_cell(cell)`
Moves the platform to be over a cell.
Computes the actual position to move to using cell size from the config.
If the expected error is over a preset threshold, first performs a position reset via `go_to_edge()` and then performs the movement.

**Assumptions**:

- *None*

**Effects**:

- If the expected error is over the threshold, performs a reset.
- The physical platform moves to have the grabber centred over the supplied cell row.
- Internal position is updated by the actual distance moved, with the result being "sufficiently close" to the centre of the desired cell row.
- Expected error is incremented by a factor of the actual distance moved.

### `go_to_edge()`
Moves the platform to the minimum row edge of the active area until the reset button is pressed.
On reset button press, stops the platform, sets internal position to the preconfigured edge position and resets expected error to zero.

**Assumptions**:

- *None*

**Effects**:

- The physical platform moves to the minimum row edge of the active area.
- Internal position is set to preconfigured edge position.
- Expected error is set to zero.

### `centre()`
Moves the platform into the centre of the top rail.
Serves to even the load on the arch motors.

**Assumptions**:

- *None*

**Effects**:

- The physical platform moves to the middle of the top rail.
- Internal position is updated by the actual distance moved, with the result being "sufficiently close" to the centre of the top rail.
- Expected error is incremented by a factor of the actual distance moved.

## Grabber
Public state:

- `position`: whether the grabber is in the `up` position, `down` position or `board` position.
- `on`: true when the electromagnet is turned on, false otherwise.

### `go_up()`
Moves the grabber into the up position.
This position is just below the platform.

**Assumptions**:

- The grabber is not in the up position.

**Effects**:

- The grabber is in the up position.
- The state variable `position` is set to `up`.

### `go_down(piece, adjust)`
Moves the grabber into the down position.
This position is at the top of a piece identified in the argument.
There is also an optional adjustment (positive is up) - this is mainly used to compensate for bend in the top rail.

**Assumptions**:

- The grabber is not in the down position.

**Effects**:

- The grabber is in the down position.
- The state variable `position` is set to `down`.

### `go_to_board()`
Moves the grabber into the board position.
This position is just above the board.

**Assumptions**:

- The grabber is not in the board position.

**Effects**:

- The grabber is in the board position.
- The state variable `position` is set to `board`.

### `turn_on()`
Turns the electromagnet on.

**Assumptions**:

- *None*

**Effects**:

- The electromagnet is turned on.
- The state variable `on` is set to true.

### `turn_off()`
Turns the electromagnet off.

**Assumptions**:

- *None*

**Effects**:

- The electromagnet is turned off.
- The state variable `on` is set to false.

## Notes
- Error increment factors are based on testing.
- Noted state does not include the internal state like maximum speed or wheel circumference.
- Space between board and buffer could be handled by code similar to `if column > 7: target += config.buffer_offset`.
- Origin of the coordinate system is at the lower left corner of A1, with positive axes going right, forward and up.
- Cell coordinates are represented by column-row pairs containing zero-based indices (e.g. C5 is `(2,4)`).
