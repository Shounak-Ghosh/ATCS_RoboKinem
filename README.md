# ATCS: Robotics Kinematics Software

## Dependencies
```
python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
python -m pip install adafruit-circuitpython-servokit
```
All code formatted in accordance with `flake8`.

## Connecting to and transferring code to the robot
First, we need to find the Rasberry Pi's IP.

- Power on and connect the robot to a monitor-keyboard-mouse setup.
- Ensure the Pi has full network access (ex. [login.harker.org](url))
- Open Terminal and run `ifconfig`. Note the IP in the general form (xx.xx.xx.xx) in the first line of the last block of output text.
- Disconnect the robot from the setup.

Now we must establish a connection between the Pi and our local device.

- Download [FileZilla](https://filezilla-project.org) and connect via the application prompts.
  - Ex. Host: `xx.xx.xx.xx`, Username: pi, Password: kinematics22, Port: 22
- Transfer files accordingly via the FileZilla application.
- Use `ssh pi@xx.xx.xx.xx` on our local terminal. Once a connection is established, we can execute python files on the Pi.



