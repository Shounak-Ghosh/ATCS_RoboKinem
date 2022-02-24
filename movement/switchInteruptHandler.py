# RPi.GPIO documentation
# https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html

# Code heavily based on the article below
# https://raspi.tv/2013/how-to-use-interrupts-with-python
# -on-the-raspberry-pi-and-rpi-gpio

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO 26 set up as input. It is pulled up to stop false signals
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Make sure you have a button connected so that when pressed")
print("it will connect GPIO port 26 to GND \n")
raw_input("Press Enter when ready\n>")

print("Waiting for falling edge on port 26")
# now the program will do nothing until the signal on port 26
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

print("During this waiting time, your computer is not")
print("wasting resources by polling for a button press.\n")
print("Press your button when ready to initiate a falling edge interrupt.")
try:
    GPIO.wait_for_edge(26, GPIO.FALLING)
    print("\nFalling edge detected. Now your program can continue with")
    print("whatever was waiting for a button press.")
except KeyboardInterrupt:
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
GPIO.cleanup()  # clean up GPIO on normal exit