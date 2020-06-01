import socket
import constants
import dataTranslation

packetLossCount = 0
ySpeed = 0.0
xSpeed = 0.0
zRotation = 0.0

print ("Setting up UDP communication socket on " + constants.UDP_IP + ":" + str(constants.UDP_PORT))
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((constants.UDP_IP, constants.UDP_PORT))
print ("Setup communication socket!")

print ("Starting receive loop...")
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #data = "2.0,0.2,-0.7"
    print ("received message:", data)
    checkedPacket, valditity = dataTranslation.decodeData(data)
    if (valditity == True):
        print("Received valid packet! | {} , {} , {}".format(checkedPacket[0], checkedPacket[1], checkedPacket[2]))
    else:
        global packetLossCount
        packetLossCount += 1
        print ("ERROR: invalid packet received: {}".format(packetLossCount))