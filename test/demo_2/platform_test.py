# Platform movement test.
# This script sets up the platform and then runs it side to side a certain number of times, reporting error statistics at the end.
#
# Author(s):
#   Jeremy Scott
#   Filip Smola

import sys
import math

from low_level import platform as p
from low_level import config
from low_level import motor

def run():
    # Instantiate platform
    platform = p.Platform()
    
    # Run experiment
    n = 20
    print("=== Experiment (n = %d) ==" % (n))
    left_errors = []
    # centre_errors will have double the number of entries than left_errors or right_errors
    centre_errors = []
    right_errors = []
    for i in range(0, n):
        print("Iteration %d" % (i))
    
        # Go left
        platform.go_to_cell((4,4))
        left_errors.append(platform.error)
        
        # Go centre
        platform.centre()
        centre_errors.append(platform.error)
    
        # Go right
        platform.go_to_cell((-4,-4))
        right_errors.append(platform.error)
        
        # Go centre
        platform.centre()
        centre_errors.append(platform.error)
    
    # Compute and print left statistics
    print("=== Statistics (n = %d) ===" % (n))
    left_max_abs = 0
    left_min_abs = sys.maxsize
    left_avg = 0
    for x in left_errors:
        if math.fabs(x) > left_max_abs:
            left_max_abs = math.fabs(x)
    
        if math.fabs(x) < left_min_abs:
            left_min_abs = math.fabs(x)
    
        left_avg += x
    left_avg /= n
    print("LEFT: max_abs = %d, min_abs = %d, avg = %f" % (left_max_abs, left_min_abs, left_avg))
    
    # Compute and print centre statistics
    centre_max_abs = 0
    centre_min_abs = sys.maxsize
    centre_avg = 0
    for x in centre_errors:
        if math.fabs(x) > centre_max_abs:
            centre_max_abs = math.fabs(x)
    
        if math.fabs(x) < centre_min_abs:
            centre_min_abs = math.fabs(x)
    
        centre_avg += x
    centre_avg /= n
    print("CENTRE: max_abs = %d, min_abs = %d, avg = %f" % (centre_max_abs, centre_min_abs, centre_avg))

    # Compute and print right statistics
    right_max_abs = 0
    right_min_abs = sys.maxsize
    right_avg = 0
    for x in right_errors:
        if math.fabs(x) > right_max_abs:
            right_max_abs = math.fabs(x)
    
        if math.fabs(x) < right_min_abs:
            right_min_abs = math.fabs(x)
    
        right_avg += x
    right_avg /= n
    print("RIGHT: max_abs = %d, min_abs = %d, avg = %f" % (right_max_abs, right_min_abs, right_avg))