import time
import numpy as np
import Matrices.frame as fr
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO  # control through GPIO pins

# adafruit forces GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
# I2C for PCS9685 and Gyro
# create i2c bus interface to access PCA9685, for example
i2c = busio.I2C(SCL, SDA)    # busio.I2C(board.SCL, board.SDA) create i2c bus
pca = PCA9685(i2c, address=0x41)           # adafruit_pca9685.PCA9685(i2c)   instance PCA9685 on bus
pca.frequency = 50  # set pwm clock in Hz (debug 60 was 1000)
# usage: pwm_channel = pca.channels[0] instance example
#        pwm_channel.duty_cycle = speed (0 .. 100)  speed example

L0 = 75
L1 = 177
L2 = 105

speed = 90 # degree per second

currentLoc = None

PWMOEN = 4  # pin 7 #PCA9685 OEn pin
pwmOEn = GPIO.setup(PWMOEN, GPIO.OUT)  # enable PCA outputs

R1 = pca.channels[0]
R2 = pca.channels[1]
R3 = pca.channels[2]
R4 = pca.channels[3]
R5 = pca.channels[15]
clawRange = [70,30]


# equivalent of Arduino map()
def valmap(value, istart, istop, ostart, ostop): 
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

# for 0 to 100, % speed as integer, to use for PWM 
# full range 0xFFFF, but PCS9685 ignores last Hex digit as only 12 bit resolution)
def getPWMPer(value): 
    if value < 0:
      value = 0
      print("Angle is below range")
    if value > 180:
      value = 180
      print("Angle is above range")
    return int(valmap(value, 0, 180, 2038, 12.5/100 * 0xFFFF))

def zeroArm():
    R1.duty_cycle = getPWMPer(90)
    R2.duty_cycle = getPWMPer(90)
    R3.duty_cycle = getPWMPer(180)
    R4.duty_cycle = getPWMPer(90)
    R5.duty_cycle = getPWMPer(90)

def unscrew(direction=True, end=False):
  R4.duty_cycle = getPWMPer(180)
  time.sleep(0.5)
  R5.duty_cycle = getPWMPer(clawRange[0])
  time.sleep(0.5)
  R4.duty_cycle = getPWMPer(0)
  time.sleep(0.5)
  if not end:
    R5.duty_cycle = getPWMPer(50)
    time.sleep(0.5)

def moveTo(point, old, instant=False):
    beta = np.deg2rad(point[3])
    alpha = (point[2][0]) # kept in degrees
    x = point[0]
    y = point[1]
    p2 = None
    if beta > 90:
      x2 = x + L1 * np.cos(beta)
      y2 = y + L1 * np.sin(beta)
      p2 = [x2, y2]
    else:
      x2 = x - L1 * np.cos(beta)
      y2 = y - L1 * np.sin(beta)
      p2 = [x2, y2]
    print(x2,y2)
    t2 = np.arctan2(p2[1], p2[0])
    t1 = (np.pi/2 - t2) + beta + np.pi/2
    print(np.rad2deg(t1), np.rad2deg(t2))

    delta = [t1 - old[0], t2 - old[1], alpha - old[2]]

    print(delta)

    maxTheta = np.rad2deg(max([delta[0], delta[1]]))

    print("maxTheta", maxTheta)

    if instant:
      R1.duty_cycle = getPWMPer(alpha)
      R2.duty_cycle = getPWMPer(np.rad2deg(t2))
      R3.duty_cycle = getPWMPer(np.rad2deg(t1))
    else:
      for i in range(int(maxTheta)):
        percent = i / maxTheta
        R1.duty_cycle = getPWMPer(old[2] + percent * delta[2])
        R2.duty_cycle = getPWMPer(np.rad2deg(old[1] + percent * delta[1][0]))
        R3.duty_cycle = getPWMPer(np.rad2deg(old[0] + percent * delta[0][0]))
        time.sleep(1/(speed))

    time.sleep(0.5) # remove after speed implementation

    if point[4]:
      R5.duty_cycle = getPWMPer(clawRange[0])
    else:
      R5.duty_cycle = getPWMPer(clawRange[1])
    return [t1,t2,alpha]

# points using coords [x,y,thetaBase, thetaClaw, grabbing] in mm and degrees:
initLoc = [[0], [205], [0], [90], False]
over = [[100], [105], [30], [0], True]
under = [[-105], [100], [180], [90], False]
test = [[167], [114], [0], [27], False]
nutLoc = [[122], [81], [36.5], [-15], False]
backLoc = [[40], [85], [36.5], [-15], True]
screwLoc = [[100], [0], [-30], [140], True]


# while True:
temp = [np.pi,np.pi/2,0]
temp = moveTo(initLoc, temp, instant=True)
# temp = moveTo(over, temp)
# #temp = moveTo(under, temp)
# temp = moveTo(test, temp)
temp = moveTo(nutLoc, temp)
for i in range(2):
  unscrew()
unscrew(end=True)

temp = moveTo(backLoc, temp)
temp = moveTo(initLoc, temp)
