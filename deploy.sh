#! /bin/bash

# Copies select directories and start script to /home/robot/robot on the EV3 brick.
#
# Authors:
#   Filip Smola

remote="robot@ev3dev:/home/robot/robot"
files="start.sh stop.py ./test"

scp -r $files $remote
