# Dummy implementations of the High Level Interface.
# These implementations only change internal state and print commands to standard output.
# They do not control any hardware.
#
# Author(s):
#   Stewart Wilson
#   Filip Smola

from . import config

preset_state = ('L', 1)
current_state = ('L', 1)


# Dummy Arch
class High_Level_Interface:

    # Move piece to empty square
    def move_piece(self, cellA, cellB, piece_type = 'default'):
        self.move(cellA, cellB)
        self.reset()


    # Move piece in cellA to cellB
    def move(self, cellA, cellB, piece_type = 'default'):
        # Pretend
        print("Moving piece at %s to %s" % (cellA, cellB))

    # Go to reset by going to preset state
    def reset(self):
        # Pretend
        print("Moving robot to preset state/cell")

        # Changing state to preset cell
        self.current_state = preset_state

    # Run calibration
    def calibrate(self):
        print("Calibrating...")
        self.reset()
        input("Move frame so the grabber is over centre of L1, then press Enter.")
        print("Calibrated")

    # Take piece in cellB and replace with one in cellA
    def take_piece(self, cellA, cellB, piece, piece_type_A = 'default', piece_type_B = 'default'):
        # Get buffer cell for piece
        buffer_cell = config.buffer_cell(piece)

        self.move(cellB, buffer_cell)
        self.move(cellA, cellB)
        self.reset()

    # Castling function (May need reworked)
    def perform_castling_at(self, cellA, cellB, cellC, cellD, piece, piece_type_A = 'default', piece_type_B = 'default'):
        self.move(cellA, cellC)
        self.move(cellB, cellD)
        self.reset()

    # En passant from cellA to cellB and taking from cellTake
    def en_passant(self, cellA, cellB, cellTake, piece):
        self.move(cellA, cellB)
        self.move(cellTake, config.buffer_cell(piece))
        self.reset()


hli = High_Level_Interface()
