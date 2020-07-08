# Data Translation and Verifying Module
import constants

# Clamps a list of numbers to a max and min
def clampList(dataList, min_value, max_value):
    clampedData = []
    for x in (dataList):
        clampedNumber = max(min(x, max_value), min_value)
        clampedData = clampedData + [clampedNumber]
    return clampedData

# Takes in data, decodes and checks for validitity
def decodeData(_data):
    try:
        dataSeperated = _data.split(',')
        if not (len(dataSeperated) == constants.expectedPacketLength):
            raise Exception("Accepted packet is not the expected length. Expected: {}, Received: {}".format(constants.expectedPacketLength, len(dataSeperated)))
        dataSeperated = [float(loopData) for loopData in dataSeperated]
        clampedData = clampList(dataSeperated, -1.0, 1.0);
    except Exception as e:
        return [0.0,0.0,0.0,0.0], False;
    else:
        return clampedData, True;