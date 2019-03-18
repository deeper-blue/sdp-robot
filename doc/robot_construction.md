> Note: This file is an excerpt from the project's User Guide.

# Hardware Setup

## Components
TODO mention EV3?

The robot consists of the following components:

- Board
- Base frame: frame on which the Arch moves.
- Arch: moves the rest of the robot along the rows of the board.
- Platform: moves the grabber along the columns of the board.
- Grabber: holds a piece as it is moved around the board.

### Board
This is a sheet of paper with a grey rectangle, containing one full chess board and one half of a chess board.
The grey rectangle servers as a guide for placing the Base Frame.
The full chess board is where the game is played.
The half of a chess board is buffer space for taken pieces.
Each piece has a preallocated place in the buffer.

### Base Frame
This is a rectangular frame that sits around the board.
It provides the rails for the Arch to move on, as well as a reference point against which the Arch resets.

### Arch
This is the biggest moving part of the robot.
It consists of the two top rails (on which tha Platform sits), one leg on each side and a motor at the bottom of each leg.
It is responsible for moving the robot along the rows of the board.
The Arch also has a touch sensor on one of its legs.
This is used to reset its position and avoid accumulating error.

### Platform
This is a small "car" on top of the Arch.
It holds the grabber and is responsible for moving it along the columns of the board.
The Platform also has a touch sensor on one of its ends.
This is used to reset its position and avoid accumulating error.

### Grabber
This is the electromagnet suspended from the Platform.
It is responsible for holding a piece as it is moved around the board.
The electromagnet is powered by a separate battery pack and the flow of power to it is controller from Port 3 on the EV3 through a dedicated circuit.

TODO sensor?

## Assembly
TODO: fix numbering

1. Attach spreaders to bottom rails to form the rectangualar Base Frame.
    It should follow the outline of the grey square on the board.
    The spreader with a small wall on top of it should be placed with the wall at the top-right corner of the buffer space.
2. Assemple the Arch by attaching the top rails to the top corners of the Arch legs with provided connectors.
3. Place Arch on the Base Frame with motor ports of the Arch legs facing towards decreasing board columns and the reset button facing the small wall on the spreader.
3. Attach reset barrier to the Arch leg closer to row 1.
3. Attach strengthening pieces to corners of the Arch.
4. Attach the EV3 and circuit holder to the top rails.
    **TODO**: this will need a picture, or very long description
5. Place the Platform on the top rail with its reset button facing toward decreasing rows and the barrier on one of the legs.
    In order to improve wheel alignment, align the ends of one of the axles with the legs of the EV3 and circuit holder.
6. Place the EV3 into the smaller slot on the holder, and the circuit box into the larger slot on the holder.
    While placing the circuit box, take care to keep the yellow and orange wires going under the box around the inner side (this is to aid Grabber connection).
7. Connect all motors and sensors to the EV3 ports indicated by labels on the devices using the accordingly labeled cables.
    If any of the cables are hanging loosely, you can use special points on the structure to secure them (**TODO** pictures).
8. Connect the Grabber control circuit to Port 3 of the EV3.
9. Connect the reb-black wire on the Platform to the yellow-orange wire from the Grabber control circuit (the orientation doesn't matter).
    Again, make sure the connection is made through the centre of the EV3 and circuit holder.
    This way there is minimal chance of the wire interfering with the Platform's movement.

# Hardware Use

## Power
TODO charging
TODO circuit batteries

## Turning the Robot On
TODO

## Maintenance
TODO

---
# TODOs, Notes and Questions
- How will we be shipping the board? A paper with grey rectangle, board and buffer like now?
- Probably replace "robot" with actual robot name.
- Component breakdown is there mainly to not have to explain what is what in assembly section.
- List at start of Components might be redundant?
- Assembly instructions will **need** pictures.
