import socket
import threading
import constants
import dataTranslation
import serial
import stepper
#import RPi.GPIO as GPIO

try:
    packetLossCount = 0

    frontRightWheelSpeed = 0.0
    frontLeftWheelSpeed = 0.0
    backRightWheelSpeed = 0.0
    backLeftWheelSpeed = 0.0

    debug = True

    #stepper.initGPIO()

    #Start Motors disabled
    #stepper.disableMotors()

    print ("Setting up UDP communication socket on " + constants.UDP_IP + ":" + str(constants.UDP_PORT))
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((constants.UDP_IP, constants.UDP_PORT))
    print ("Setup communication socket!")

    print("Setting up Serial between Raspberry Pi and Leonardo.")
    ser = serial.Serial(constants.SERIAL_PORT, constants.SERIAL_BUADRATE)
    print("Serial port information: ")
    print("    Port: " + constants.SERIAL_PORT)
    print("    Buadrate: " + str(constants.SERIAL_BUADRATE))

    def tell(msg):
        msg = '<' + msg + '>'
        msg = msg.encode('ascii') # encode n send
        ser.write(msg)

    # Wont be used much be is there if needed
    def hear():
        while True:
            if ser.inWaiting > 0:
                msg = ser.read_until()
                decodedString = msg.decode('ascii').rstrip()
                print("Serial | Received serial: " + decodedString)

    # print("Setting up serial receive thread.")
    # SerialReceiveThread = threading.Thread(target=hear)
    # SerialReceiveThread.start()
    # print("Setup receive thread")

    #stepper.enableMotors()

    print ("Starting main loop...")
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #data = "2.0,0.2,-0.7"
        #print ("received message:", data.decode())
        checkedPacket, valditity = dataTranslation.decodeData(data.decode())

        if (valditity == True):
            print("Socket | Received valid packet! : {} , {} , {} , {}".format(checkedPacket[0], checkedPacket[1], checkedPacket[2], checkedPacket[3]))
            #FL, FR, BL, BR
            tell((str(int(checkedPacket[0]*constants.MAX_STEP_RATE)) + ',' + str(int(checkedPacket[1]*constants.MAX_STEP_RATE)) + ',' + str(int(checkedPacket[2]*constants.MAX_STEP_RATE)) + ',' + str(int(checkedPacket[3]*constants.MAX_STEP_RATE))))
        else:
            packetLossCount += 1
            print ("Socket | ERROR: invalid packet received. : {}".format(packetLossCount))
except KeyboardInterrupt:
    #GPIO.cleanup()
    print("Manual Shutdown.")
finally:
    print("Final Cleanup...")
    #GPIO.cleanup()