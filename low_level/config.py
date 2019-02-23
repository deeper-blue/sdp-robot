# This file is used to hold the different measurements of the chess board, which will be used in the implementation of the robot.
# Allows us to abstract from the main program.
#
# Author(s):
#   Jeremy Scott
#   Filip Smola

#--- Start Configuration

# The length of one side of a square on the chess board in cm
square_length = 3.8

# Total length of row in cm (start of board to end of buffer)
row_length = 58

# Total length of the columns in cm (top platform)
column_length = 50

# The length from the end of the last row to the start of the buffer in cm
buffer_offset = 12

# Height of the board in cm
board_height = 2.4

# Tallest piece in cm
tallest_piece = 7.9

# Wheel circumference in cm
wheel_circ = 12.8

# Grabber height in cm
grabber_height = 24.9

# Grabber wheel circumference in cm
grabber_circ = 7.06

# Port of grabber motor
grabber_motor_port = 'outD'

# Port of the left motor for the arch
left_arch_motor = 'outA'

# Port of the right motor for the arch
right_arch_motor = 'outB'

# Port of the motor for the platform
platform_motor = 'outC'

# Port for the touch sensor for the arch
touch_sensor_arch = 'in2'

# Port for the touch sensor for the platform
touch_sensor_platform = 'in1'

#--- End Configuration

#--- Start Processing

# Cell column to cm along bottom rail
def cell_column_cm(n):
    # Naive position
    cm = n * square_length

    # Adjust for buffer offset
    if n > 7:
        cm += buffer_offset

    return cm

# Cell row to cm along the top rail
def cell_row_cm(n):
    return n * square_length

# Arch reset position is its maximum position
arch_reset_position = row_length

# Platform reset position is origin
platform_reset_position = 0

# Centre of top rail
top_centre = column_length / 2

#--- End Processing
