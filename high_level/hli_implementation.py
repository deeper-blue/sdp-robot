# Implementations of the High Level Interface.
# Implementation used to with low level dummy implementation
#
# Author(s):
#   Stewart Wilson
#   Filip Smola

import time
from . import config
from low_level.dummy import arch, platform, grabber

preset_state = ('L', 1)

# Time to wait around grabber up/down (in second)
grabber_wait = 1

# Compute adjustment needed based on platform position
def adjust(plat):
    x = plat / config.top_bend_range - 0.5
    return config.top_bend_max * (x * x)

# Dummy Arch
class High_Level_Interface:

    def __init__(self, current_state, arch, platform, grabber):
        self.current_state = current_state
        self.arch = arch
        self.platform = platform
        self.grabber = grabber

    # Move frame to cell
    def go_to_cell(self, cell, converted = False):
        if not converted:
            cell = config.convert_cell(cell)
        self.platform.centre()
        self.arch.go_to_cell(cell)
        self.platform.go_to_cell(cell)

    # Pick a piece up (includes waiting)
    def pick_up(self):
        time.sleep(grabber_wait)
        self.grabber.go_down(adjust(self.platform.position))
        self.grabber.turn_on()
        self.grabber.go_up()
        time.sleep(grabber_wait)

    # Put a piece down (includes waiting)
    def put_down(self):
        time.sleep(grabber_wait)
        self.grabber.go_down(adjust(self.platform.position))
        self.grabber.turn_off()
        self.grabber.go_up()
        time.sleep(grabber_wait)

    # Move piece to empty square
    def move_piece(self, cellA, cellB):
        self.move(cellA, cellB)
        self.reset()

    # Move piece in cellA to cellB
    def move(self, cellA, cellB):
        print("Moving piece at %s to %s\n" % (cellA, cellB))

        # Convert cells if their first isn't an integer
        if not isinstance(cellA[0], int):
            cellA = config.convert_cell(cellA)
        if not isinstance(cellB[0], int):
            cellB = config.convert_cell(cellB)

        # Move to cellA -> pick up -> move to cellB -> place
        self.go_to_cell(cellA, True)
        self.pick_up()
        self.go_to_cell(cellB, True)
        self.put_down()

    # Go to reset by going to preset state
    def reset(self):
        print("Moving robot to preset state/cell")

        # Centre platform and go to preset/reset position
        self.platform.centre()
        self.arch.go_to_edge()
        self.platform.go_to_edge()

        # Changing state to preset cell
        self.current_state = preset_state

    # Run calibration
    def calibrate(self):
        print("Calibrating...")
        self.reset()
        self.grabber.go_down()
        input("Move frame so the grabber is over centre of L1, then press Enter.")
        self.grabber.go_up()
        print("Calibrated")


    # Take piece in cellB and replace with one in cellA
    def take_piece(self, cellA, cellB, piece):
        # Get buffer cell for piece
        buffer_cell = config.buffer_cell(piece)

        print("Taking piece, %s, at %s with piece at %s\n" % (piece, cellB, cellA))
        self.move(cellB, buffer_cell)
        self.move(cellA, cellB)
        self.reset()

    # Castling function (May need reworked)
    def perform_castling_at(self, cellA, cellB, cellC, cellD):
        print("Peforming Castling at %s and %s\n" % (cellA, cellB))

        self.move(cellA, cellC)
        self.move(cellB, cellD)
        self.reset()

    # En passant from cellA to cellB and taking from cellTake
    def en_passant(self, cellA, cellB, cellTake, piece):
        print("Performing en passant from %s to %s, taking %s from %s" % (cellA, cellB, piece, cellTake))

        self.move(cellA, cellB)
        self.move(cellTake, config.buffer_cell(piece))
        self.reset()

hli = High_Level_Interface(preset_state, arch, platform, grabber)
