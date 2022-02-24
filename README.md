# ATCS: Robotics Kinematics Software

## Dependencies
```
pip install numpy
pip install matplotlib
python -m pip install adafruit-circuitpython-servokit
```
All code formatted in accordance with `flake8`.

## Connecting to and transferring code to the robot
First, we need to find the Rasberry Pi's IP.

- Power on and connect the robot to a monitor-keyboard-mouse setup.
- Ensure the Pi has full network access (ex. [login.harker.org](url))
- Open Terminal and run `ifconfig`. Note the IP in the form (xx.xx.xx.xx) in the first line of the last block of output text.
- Disconnect the robot from the setup and power off.

Now we must establish a connection between the Pi and our local device.

- Download FileZilla and connect via the application prompts.
  - Ex. Username: pi, Password: kinematics2022
- Use `ssh pi@xx.xx.xx.xx` on our local terminal.


