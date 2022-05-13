import time
import numpy as np
import frame as fr
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO #control through GPIO pins

# adafruit forces GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
#I2C for PCS9685 and Gyro
# create i2c bus interface to access PCA9685, for example
i2c = busio.I2C(SCL, SDA)    #busio.I2C(board.SCL, board.SDA) create i2c bus
pca = PCA9685(i2c, address = 0x41)           #adafruit_pca9685.PCA9685(i2c)   instance PCA9685 on bus
pca.frequency = 50 #set pwm clock in Hz (debug 60 was 1000)
# usage: pwm_channel = pca.channels[0] instance example
#        pwm_channel.duty_cycle = speed (0 .. 100)  speed example

PWMOEN = 4 #pin 7 #PCA9685 OEn pin
pwmOEn = GPIO.setup(PWMOEN, GPIO.OUT)  # enable PCA outputs

R1 = pca.channels[0]
R2 = pca.channels[1]
R3 = pca.channels[2]
R4 = pca.channels[3]
R5 = pca.channels[4]

#equivalent of Arduino map()
def valmap(value, istart, istop, ostart, ostop): 
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

#for 0 to 100, % speed as integer, to use for PWM 
#full range 0xFFFF, but PCS9685 ignores last Hex digit as only 12 bit resolution)
def getPWMPer(value): 
  return int(valmap(value, 0, 180, 2038, 12.5/100 * 0xFFFF))
# while True:
R1.duty_cycle = getPWMPer(90)
R2.duty_cycle = getPWMPer(90)
R3.duty_cycle = getPWMPer(90)
R4.duty_cycle = getPWMPer(90)
R5.duty_cycle = getPWMPer(90)

while True:
    for i in range(180):
        R3.duty_cycle = getPWMPer(i)
        time.sleep(0.02)
        print(i)
    time.sleep(1)
    for i in range(180):
        R3.duty_cycle = getPWMPer(180-i)
        time.sleep(0.02)
        print(180-i)
    time.sleep(1)