import socket
import constants
import dataTranslation
import dataManipulation
import stepper
import threading
import queue

packetLossCount = 0

frontRightWheelSpeed = 0.0
frontLeftWheelSpeed = 0.0
backRightWheelSpeed = 0.0
backLeftWheelSpeed = 0.0

stepper.initGPIO()

#Start Motors disabled
stepper.disableMotors()

print ("Setting up UDP communication socket on " + constants.UDP_IP + ":" + str(constants.UDP_PORT))
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((constants.UDP_IP, constants.UDP_PORT))
print ("Setup communication socket!")

print ("Setting up stepper threads and respective queues...")
FL_Queue = queue.Queue()
FR_Queue = queue.Queue()
BL_Queue = queue.Queue()
BR_Queue = queue.Queue()

FLThread = threading.Thread(target=stepper.driveStepper, args=(constants.FL_STEP, constants.FL_DIR, FL_Queue,)).start()
FRThread = threading.Thread(target=stepper.driveStepper, args=(constants.FR_STEP, constants.FR_DIR, FR_Queue,)).start()
BLThread = threading.Thread(target=stepper.driveStepper, args=(constants.BL_STEP, constants.BL_DIR, BL_Queue,)).start()
BRThread = threading.Thread(target=stepper.driveStepper, args=(constants.BR_STEP, constants.BR_DIR, BR_Queue,)).start()
print ("Setup threads and queues!")

stepper.enableMotors()

print ("Starting receive loop...")
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #data = "2.0,0.2,-0.7"
    print ("received message:", data)
    checkedPacket, valditity = dataTranslation.decodeData(data)

    if (valditity == True):
        print("Received valid packet! | {} , {} , {}".format(checkedPacket[0], checkedPacket[1], checkedPacket[2]))
        #FL, FR, BL, BR
        wheelspeeds = dataManipulation.calculateAllWheelSpeeds(checkedPacket[0], checkedPacket[1], checkedPacket[2])
        FL_Queue.put(wheelspeeds[0])
        FR_Queue.put(wheelspeeds[1])
        BL_Queue.put(wheelspeeds[2])
        BR_Queue.put(wheelspeeds[3])
    else:
        global packetLossCount
        packetLossCount += 1
        print ("ERROR: invalid packet received: {}".format(packetLossCount))
        FL_Queue.put(0.0)
        FR_Queue.put(0.0)
        BL_Queue.put(0.0)
        BR_Queue.put(0.0)
    


    