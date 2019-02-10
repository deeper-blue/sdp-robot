# Low Level Interface
Description of the low-level interface.

## Arch
Public state:

- `position`: the position of the arch along the bottom rail in cm.
- `expected_error`: the expected error in cm, computed as `error = internal_position - real_position`.
    How much the arch would have to move to really be at internal position.

### `go_to_position(position)`
Moves the arch to absolute position along the bottom rail.
The `position` argument is in cm.

**Assumptions**:

- The platform is in the centre (even load on motors).

**Effects**:

- The physical arch moves to the supplied position.
- Internal position is updated by the actual distance moved, with the result being "sufficiently close" to the desired value.
- Expected error is incremented by a factor of the actual distance moved.

### `go_to_cell(cell)`
Moves the arch to be over a cell.
Computes the actual position to move to using cell size from the config.

**Assumptions**:

- The platform is in the centre (even load on motors).

**Effects**:

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

### `on_button_press()`
Handles unintentional reset button presses.
Sets internal position to the preconfigured edge position and resets expected error to zero.

**Assumptions**:

- *None*

**Effects**:

- Internal position is set to preconfigured edge position.
- Expected error is set to zero.

## Platform
Public state:

- `position`: the position of the platform along the top rail in cm.
- `expected_error`: the expected error in cm, computed as `error = internal_position - real_position`.
    How much the platform would have to move to really be at internal position.

### `go_to_position(position)`
Moves the platform to absolute position along the top rail.
The `position` argument is in cm.

**Assumptions**:

- *None*

**Effects**:

- The physical platform moves to the supplied position.
- Internal position is updated by the actual distance moved, with the result being "sufficiently close" to the desired value.
- Expected error is incremented by a factor of the actual distance moved.

### `go_to_cell(cell)`
Moves the platform to be over a cell.
Computes the actual position to move to using cell size from the config.

**Assumptions**:

- *None*

**Effects**:

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

### `on_button_press()`
Handles unintentional reset button presses.
Sets internal position to the preconfigured edge position and resets expected error to zero.

**Assumptions**:

- *None*

**Effects**:

- Internal position is set to preconfigured edge position.
- Expected error is set to zero.

## Grabber
Public state:

- `up`: true when the grabber is in the up position, false otherwise.
- `on`: true when the electromagnet is turned on, false otherwise.

### `go_up()`
Moves the grabber into the up position.

**Assumption**:

- The grabber is in the down position.

**Effects**:

- The grabber is in the up position.
- The state variable `up` is set to true.

### `go_down()`
Moves the grabber into the down position.

**Assumption**:

- The grabber is in the up position.

**Effects**:

- The grabber is in the down position.
- The state variable `up` is set to false.

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
- There is redundancy between the functions "go_to_position" and "go_to_cell" if we decide to include the buffer as valid 
cells. This, therefore, means that we may just consider implementing the function "go_to_cell". This would be more 
computationally complex as we will have to take into account things like the distance between the end of the final column 
and the start of the buffer. A possible solution to this could be; "if column > 8: config.buffer_offset".

## TODO
- Where is the origin of the coordinate system? At A1 of the board?
- How are out-of-board locations handles (e.g. buffer)? Extending the cell space there?
- What is sufficiently close? Accurate to 1% of the entire rail length?
- Do we want to handle unintentional reset button presses?
- Which side does the platform reset on?
