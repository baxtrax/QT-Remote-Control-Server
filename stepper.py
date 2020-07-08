import constants
import queue
from time import sleep
import RPi.GPIO as GPIO

def initGPIO():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(constants.B_M0, GPIO.IN)
    GPIO.setup(constants.B_M1, GPIO.IN)
    GPIO.setup(constants.B_M2, GPIO.IN)
    GPIO.setup(constants.F_M0, GPIO.IN)
    GPIO.setup(constants.F_M1, GPIO.IN)
    GPIO.setup(constants.F_M2, GPIO.IN)

def enableFrontMotors():
    GPIO.output(constants.F_ENA, GPIO.LOW)

def enableBackMotors():
    GPIO.output(constants.B_ENA, GPIO.LOW)

def disableFrontMotors():
    GPIO.output(constants.F_ENA, GPIO.HIGH)

def disableBackMotors():
    GPIO.output(constants.B_ENA, GPIO.LOW)

def enableMotors():
    enableFrontMotors()
    enableBackMotors()

def disableMotors():
    disableFrontMotors()
    disableFrontMotors()