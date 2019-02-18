# Thread Grabber movement test.
# This script sets up the thread grabber and then runs it up and down 20 times, reporting error statistics at the end.
#
# Author(s):
#   Filip Smola

import sys
import math

from low_level import grabber
from low_level import config
from low_level import motor

def run():
    # Instantiate thread grabber
    # Note: explicitly instantiating to not rely on default grabber object being thread grabber
    gr = grabber.Thread(motor.Single(config.grabber_motor_port))
    
    # Run experiment
    n = 20
    print("=== Experiment (n = %d) ==" % (n))
    up_errors = []
    down_errors = []
    for i in range(0, n):
        print("Iteration %d" % (i))
    
        # Go up
        gr.go_up()
        up_errors.append(gr.motor.get_position() - grabber.up_pos)
    
        # Go down
        gr.go_down()
        down_errors.append(gr.motor.get_position() - grabber.down_pos)
    
    # Compute and print up statistics
    print("=== Statistics (n = %d) ===" % (n))
    up_max_abs = 0
    up_min_abs = sys.maxsize
    up_avg = 0
    for x in up_errors:
        if math.fabs(x) > up_max_abs:
            up_max_abs = math.fabs(x)
    
        if math.fabs(x) < up_min_abs:
            up_min_abs = math.fabs(x)
    
        up_avg += x
    up_avg /= n
    print("UP: max_abs = %f, min_abs = %f, avg = %f" % (up_max_abs, up_min_abs, up_avg))
    
    # Compute and print down statistics
    down_max_abs = 0
    down_min_abs = sys.maxsize
    down_avg = 0
    for x in down_errors:
        if math.fabs(x) > down_max_abs:
            down_max_abs = math.fabs(x)
    
        if math.fabs(x) < down_min_abs:
            down_min_abs = math.fabs(x)
    
        down_avg += x
    down_avg /= n
    print("DOWN: max_abs = %f, min_abs = %f, avg = %f" % (down_max_abs, down_min_abs, down_avg))
