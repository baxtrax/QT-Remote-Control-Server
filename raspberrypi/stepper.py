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

    GPIO.setup(constants.F_ENA, GPIO.OUT)
    GPIO.setup(constants.B_ENA, GPIO.OUT)

    GPIO.setup(constants.FR_DIR, GPIO.OUT)
    GPIO.setup(constants.FR_STEP, GPIO.OUT)

    GPIO.setup(constants.FL_DIR, GPIO.OUT)
    GPIO.setup(constants.FL_STEP, GPIO.OUT)

    GPIO.setup(constants.BR_DIR, GPIO.OUT)
    GPIO.setup(constants.BR_STEP, GPIO.OUT)

    GPIO.setup(constants.BL_DIR, GPIO.OUT)
    GPIO.setup(constants.BL_STEP, GPIO.OUT)

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

def driveStepper(motorStepPin, motorDirPin, speed_queue):
    currentSpeed = 0.0
    print("Thread for: {} created".format(motorStepPin))
    while True:
        try:
            isEmpty = False
            speedToDrive = speed_queue.get(block=False, timeout=0)
        except queue.Empty:
            #print("Thread: Queue empty")
            isEmpty = True
        if not (isEmpty):
            currentSpeed = speedToDrive
            #print("Thread: Queue: {}".format(currentSpeed))
        
        if not (currentSpeed == 0.0):
            #If negative switch direction of step
            if (currentSpeed/abs(currentSpeed) == -1):
                GPIO.output(motorDirPin, constants.CCW)
            else:
                GPIO.output(motorDirPin, constants.CW)

            #print("Tread: Stepping")
            scaledDriveDelay = (constants.MaxSpeedDelay/abs(currentSpeed))
            GPIO.output(motorStepPin, GPIO.HIGH)
            #time to delay step = delay(0.005)/abs of current speed (0.1 etc)
            sleep(scaledDriveDelay)
            GPIO.output(motorStepPin, GPIO.LOW)
            sleep(scaledDriveDelay)