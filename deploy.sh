#! /bin/bash

# Copies select directories and start script to /home/robot/robot on the EV3 brick.
#
# Authors:
#   Filip Smola

# Check if USB connection works
count=$( ping -c 1 ev3dev | grep icmp* | wc -l )
if [ $count -eq 0 ]
then
    # Not working -> WiFi
    host="192.168.105.116"
else
    # Working -> USB
    host="ev3dev"
fi

remote="robot@$host:/home/robot/robot"
files="start.sh setup.sh qa.sh calibrate.sh stop.py test.py run.py qa.py calibrate.py ./test ./low_level ./high_level ./comms"

scp -r $files $remote
