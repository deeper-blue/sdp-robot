# Arch movement test.
# This script sets up the arch and then runs it forward and backward a certain number of times, reporting error statistics at the end.
#
# Author(s):
#   Jeremy Scott
#   Filip Smola

import sys
import math

from low_level import arch as a
from low_level import config
from low_level import motor

def run():
    # Instantiate arch
    arch = a.Arch()
    
    # Run experiment
    n = 20
    print("=== Experiment (n = %d) ==" % (n))
    forward_errors = []
    backward_errors = []
    for i in range(0, n):
        print("Iteration %d" % (i))
    
        # Go forward
        arch.go_to_cell((12,0))
        forward_errors.append(arch.error)
        
        # Reset error
        arch.go_to_edge()

        # Go backward
        arch.go_to_cell((0,0))
        backward_errors.append(arch.error)
    
    # Compute and print forward statistics
    print("=== Statistics (n = %d) ===" % (n))
    forward_max_abs = 0
    forward_min_abs = sys.maxsize
    forward_avg = 0
    for x in forward_errors:
        if math.fabs(x) > forward_max_abs:
            forward_max_abs = math.fabs(x)
    
        if math.fabs(x) < forward_min_abs:
            forward_min_abs = math.fabs(x)
    
        forward_avg += x
    forward_avg /= n
    print("FORWARD: max_abs = %d, min_abs = %d, avg = %f" % (forward_max_abs, forward_min_abs, forward_avg))
    print(forward_errors)

    # Compute and print backward statistics
    backward_max_abs = 0
    backward_min_abs = sys.maxsize
    backward_avg = 0
    for x in backward_errors:
        if math.fabs(x) > backward_max_abs:
            backward_max_abs = math.fabs(x)
    
        if math.fabs(x) < backward_min_abs:
            backward_min_abs = math.fabs(x)
    
        backward_avg += x
    backward_avg /= n
    print("BACKWARD: max_abs = %d, min_abs = %d, avg = %f" % (backward_max_abs, backward_min_abs, backward_avg))
    print(backward_errors)