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

# Compute buffer cell given the piece's original cell
def buffer_cell(original):
    # Convert cell if its first isn't an integer
    if not isinstance(original[0], int):
        original = convert_cell(original)

    (c, r) = original
    return (8 + (r % 4), c)
#--- End Processing
