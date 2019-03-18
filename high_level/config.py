# This file is used to hold the different cells in the buffer for each piece
# Allows us to abstract from the main program.
#
# Author(s):
#   Stewart Wilson
#   Filip Smola

#--- Start Configuration
# Top rail bend adjustment constants
top_bend_range = 55
top_bend_max = 0.7

# Convert cell from HLI format to LLI format
def convert_cell(cell):
    if isinstance(cell[0], int):
        return cell
    else:
        return (ord(cell[0].upper()) - 65, cell[1] - 1)

<<<<<<< HEAD
def buffer_cell(original):
    # Convert cell if its first isn't an integer
    if not isinstance(original[0], int):
        original = convert_cell(original)

    (c, r) = original
    return (8 + (r % 4), c)
||||||| merged common ancestors
buffer_cells["white_rook1"]   = ('I',1)
buffer_cells["white_knight1"] = ('I',2)
buffer_cells["white_bishop1"] = ('I',3)
buffer_cells["white_queen"]   = ('I',4)
buffer_cells["white_king"]    = ('I',5)
buffer_cells["white_bishop2"] = ('I',6)
buffer_cells["white_knight2"] = ('I',7)
buffer_cells["white_rook2"]   = ('I',8)
buffer_cells["white_pawn1"]   = ('J',1)
buffer_cells["white_pawn2"]   = ('J',2)
buffer_cells["white_pawn3"]   = ('J',3)
buffer_cells["white_pawn4"]   = ('J',4)
buffer_cells["white_pawn5"]   = ('J',5)
buffer_cells["white_pawn6"]   = ('J',6)
buffer_cells["white_pawn7"]   = ('J',7)
buffer_cells["white_pawn8"]   = ('J',8)
buffer_cells["black_pawn1"]   = ('K',1)
buffer_cells["black_pawn2"]   = ('K',2)
buffer_cells["black_pawn3"]   = ('K',3)
buffer_cells["black_pawn4"]   = ('K',4)
buffer_cells["black_pawn5"]   = ('K',5)
buffer_cells["black_pawn6"]   = ('K',6)
buffer_cells["black_pawn7"]   = ('K',7)
buffer_cells["black_pawn8"]   = ('K',8)
buffer_cells["black_rook1"]   = ('L',1)
buffer_cells["black_knight1"] = ('L',2)
buffer_cells["black_bishop1"] = ('L',3)
buffer_cells["black_queen"]   = ('L',4)
buffer_cells["black_king"]    = ('L',5)
buffer_cells["black_bishop2"] = ('L',6)
buffer_cells["black_knight2"] = ('L',7)
buffer_cells["black_rook2"]   = ('L',8)
=======
# Convert cell from HLI format to LLI format
def convert_cell(cell):
    if isinstance(cell[0], int):
        return cell
    else:
        return (ord(cell[0].upper()) - 65, cell[1] - 1)

# Compute buffer cell given the piece's original cell
def buffer_cell(original):
    # Convert cell if its first isn't an integer
    if not isinstance(original[0], int):
        original = convert_cell(original)

    (c, r) = original
    return (8 + (r % 4), c)
>>>>>>> feature/qa-scripts
#--- End Processing
