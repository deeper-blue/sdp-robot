#! /bin/bash

# Removes contents of /home/robot/robot from remote EV3 brick.
#
# Authors:
#   Filip Smola

remote="robot:maker@ev3dev"
commnad="rm -rf /home/robot/robot/*"

ssh $remote $command
