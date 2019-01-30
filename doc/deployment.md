# Deployment
This document describes the process of getting the latest version of the robot code onto the physical robot.

To enable connecting to the EV3, it needs to be connected using a USB cable.
The EV3 IP address is shown on the display of the brick.
The user on the EV3 is `robot` and password is `maker`.

## Connect to EV3
Using SSH:

```
$ ssh robot@{ip}
```

## Copy Files Onto EV3
Using SCP:

```
$ scp {local_file} robot@{ip}:{remote_file}
```

## Executing a Python File
The robot program entry point is the `start.sh` file.
To execute a python file, change the contents of the start script to run the desired file.

`TODO: fix direct execution of python files`
