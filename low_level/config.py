# This file is used to hold the different measurements of the chess board, which will be used in the implementation of the robot.
# Allows us to abstract from the main program.
#
# Author(s):
#   Jeremy Scott
#   Filip Smola

#--- Start Configuration

# The length of one side of a square on the chess board in cm
square_length = 5.09

# Total length of row in cm (start of board to end of buffer)
#row_length = 57.5

# Total length of the columns in cm (top platform)
#column_length = 35

# The length from the end of the last row to the start of the buffer in cm
buffer_offset = 2.54

# Height of the board in cm
board_height = 0

# Tallest piece in cm
tallest_piece = 3.0

# Wheel circumference in cm
wheel_circ = 12.66

# Grabber height in cm
grabber_height = 24

# Grabber wheel circumference in cm
grabber_circ = 6.6

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

# Number of the electromagnet GPIO
magnet_gpio_no = 121

# Circumference of the platform wheels in cm
platform_circ = 12.53

# Centre of top rail in cm
top_centre = 17

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

# Arch reset position is column L
arch_reset_position = cell_column_cm(11)

# Platform reset position is row 1
platform_reset_position = cell_row_cm(0)

#--- End Processing
