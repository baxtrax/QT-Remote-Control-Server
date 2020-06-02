import math

def calculateWheelDirection(y,x):
    return (math.atan2(y,x))

def calculateWheelMagnitude(y,x):
    magnitude = math.sqrt(x ** 2.0 + y ** 2.0)
    return max(min(magnitude, 1.0), 0)

def calculateFLWheelSpeed(direction, magnitude):
    return (math.sin(direction + (1/4 * math.pi))) * magnitude

def calculateFRWheelSpeed(direction, magnitude):
    return (math.sin(direction - (1/4 * math.pi))) * magnitude

def calculateBLWheelSpeed(direction, magnitude):
    return (math.sin(direction + (1/4 * math.pi))) * magnitude

def calculateBRWheelSpeed(direction, magnitude):
    return (math.sin(direction - (1/4 * math.pi))) * magnitude

#Return FL, FR, BL, BR
def calculateAllWheelSpeeds(y,x,z):
    direction = calculateWheelDirection(y, x)
    magnitude = calculateWheelDirection(y, x)
    return [calculateFLWheelSpeed(direction, magnitude),
            calculateFRWheelSpeed(direction, magnitude),
            calculateBLWheelSpeed(direction, magnitude),
            calculateBRWheelSpeed(direction, magnitude)]