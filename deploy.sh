#! /bin/bash

# Copies select directories and start script to /home/robot/robot on the EV3 brick.
#
# Authors:
#   Filip Smola

remote="robot:maker@ev3dev:/home/robot/robot"
files="start.sh ./test"

scp -r $directories $remote
