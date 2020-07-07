import socket
import constants
import dataTranslation
#import stepper
#import RPi.GPIO as GPIO

try:
    packetLossCount = 0

    frontRightWheelSpeed = 0.0
    frontLeftWheelSpeed = 0.0
    backRightWheelSpeed = 0.0
    backLeftWheelSpeed = 0.0

    #stepper.initGPIO()

    #Start Motors disabled
    #stepper.disableMotors()

    print ("Setting up UDP communication socket on " + constants.UDP_IP + ":" + str(constants.UDP_PORT))
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((constants.UDP_IP, constants.UDP_PORT))
    print ("Setup communication socket!")

    #stepper.enableMotors()

    print ("Starting receive loop...")
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #data = "2.0,0.2,-0.7"
        #print ("received message:", data.decode())
        checkedPacket, valditity = dataTranslation.decodeData(data.decode())

        if (valditity == True):
            print("Received valid packet! | {} , {} , {} , {}".format(checkedPacket[0], checkedPacket[1], checkedPacket[2], checkedPacket[3]))
            #FL, FR, BL, BR
            wheelspeeds = dataManipulation.calculateAllWheelSpeeds(checkedPacket[0], checkedPacket[1], checkedPacket[2])
            print("Calculated Wheel Speeds | {} , {} , {} , {}".format(wheelspeeds[0], wheelspeeds[1], wheelspeeds[2], wheelspeeds[3]))
        else:
            packetLossCount += 1
            print ("ERROR: invalid packet received: {}".format(packetLossCount))
except KeyboardInterrupt:
    #GPIO.cleanup()
    print("Manual Shutdown.")


    