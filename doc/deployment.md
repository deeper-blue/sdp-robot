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

## Using Deployment Scripts
There are two reployment scripts in the root of the repository - `deploy.sh` and `clean.sh`.

### `deploy.sh`
This script copies `start.sh` and the `test` directory into `/home/robot/robot` on the EV3 brick (it has to be connected via USB).
Use this script to copy the robot code onto the brick.
When you add a file or directory that you want to be deployed onto the brick, you need to add it to the `files` space-separated list in `deploy.sh`.

### `clean.sh`
This script removes all contents of the `/home/robot/robot` directory on the EV3 brick.
Use this script to clean the contents before you deploy, so no old files are left there.
