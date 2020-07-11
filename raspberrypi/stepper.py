import constants
from time import sleep
import RPi.GPIO as GPIO

def initGPIO():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(constants.F_ENA, GPIO.OUT)
    GPIO.setup(constants.B_ENA, GPIO.OUT)
    GPIO.setup(constants.B_M0, GPIO.OUT)
    GPIO.setup(constants.B_M1, GPIO.OUT)
    GPIO.setup(constants.B_M2, GPIO.OUT)
    GPIO.setup(constants.F_M0, GPIO.OUT)
    GPIO.setup(constants.F_M1, GPIO.OUT)
    GPIO.setup(constants.F_M2, GPIO.OUT)

    GPIO.output(constants.B_M0, GPIO.LOW)
    GPIO.output(constants.B_M1, GPIO.LOW)
    GPIO.output(constants.B_M2, GPIO.LOW)

    GPIO.output(constants.F_M0, GPIO.LOW)
    GPIO.output(constants.F_M1, GPIO.LOW)
    GPIO.output(constants.F_M2, GPIO.LOW)

def setFMicrostepRes(M0,M1,M2):
    GPIO.output(constants.F_M0, M0)
    GPIO.output(constants.F_M1, M1)
    GPIO.output(constants.F_M2, M2)

def setBMicrostepRes(M0,M1,M2):
    GPIO.output(constants.B_M0, M0)
    GPIO.output(constants.B_M1, M1)
    GPIO.output(constants.B_M2, M2)

def setMicrostepRes(M0,M1,M2):
    setFMicrostepRes(M0,M1,M2)
    setBMicrostepRes(M0,M1,M2)

def enableFrontMotors():
    GPIO.output(constants.F_ENA, GPIO.LOW)

def enableBackMotors():
    GPIO.output(constants.B_ENA, GPIO.LOW)

def disableFrontMotors():
    GPIO.output(constants.F_ENA, GPIO.HIGH)

def disableBackMotors():
    GPIO.output(constants.B_ENA, GPIO.HIGH)

def enableMotors():
    enableFrontMotors()
    enableBackMotors()

def disableMotors():
    disableFrontMotors()
    disableFrontMotors()
