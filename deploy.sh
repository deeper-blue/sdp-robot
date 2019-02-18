#! /bin/bash

# Copies select directories and start script to /home/robot/robot on the EV3 brick.
#
# Authors:
#   Filip Smola

remote="robot@192.168.105.$1:/home/robot/robot"
files="start.sh stop.py test.py ./test ./low_level"

scp -r $files $remote
