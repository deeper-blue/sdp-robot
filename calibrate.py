# Runs the HLI calibration function to align the board and frame at L1.
#
# Author(s):
#   Filip Smola

from test.demo_2 import hli_prepare as env

env.hli.calibrate()
