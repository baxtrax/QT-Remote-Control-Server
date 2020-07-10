/*Example sketch to control a stepper motor with DRV8825 stepper motor driver, AccelStepper library and Arduino: continuous rotation. More info: https://www.makerguides.com */

//Inver BL and FL
// Include the AccelStepper library:
#include <AccelStepper.h>

// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
#define BRdirPin 7
#define BRstepPin 6

#define FLdirPin 4
#define FLstepPin 5

#define BLdirPin 8
#define BLstepPin 9

#define FRdirPin 2
#define FRstepPin 3
#define motorInterfaceType 1

int FLSpeed = 0;
int FRSpeed = 0;
int BLSpeed = 0;
int BRSpeed = 0;

const int MaxStepSpeed = 200;
const int StepAccel = 10;

const byte numChars = 32;
const char startMarker = '<';
const char endMarker = '>';
char receivedChars[numChars];
char tempChars[numChars];

// Create a new instance of the AccelStepper class:
AccelStepper BLstepper = AccelStepper(motorInterfaceType, BLstepPin, BLdirPin);
AccelStepper BRstepper = AccelStepper(motorInterfaceType, BRstepPin, BRdirPin);
AccelStepper FLstepper = AccelStepper(motorInterfaceType, FLstepPin, FLdirPin);
AccelStepper FRstepper = AccelStepper(motorInterfaceType, FRstepPin, FRdirPin);

boolean newData = false;

void sendSpeedsToSteppers() {
  BLstepper.setSpeed(-BLSpeed);
  BRstepper.setSpeed(BRSpeed);
  FLstepper.setSpeed(-FLSpeed);
  FRstepper.setSpeed(FRSpeed);
}

void runSteppers() {
  BLstepper.runSpeed();
  BRstepper.runSpeed();
  FLstepper.runSpeed();
  FRstepper.runSpeed();
}

void recvWithStartEndMarkers() {
  static boolean recvInProgress = false;
  static byte ndx = 0;
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();

    if (recvInProgress == true) {
      if (rc != endMarker) {
        receivedChars[ndx] = rc;
        ndx++;
        if (ndx >= numChars) {
          ndx = numChars - 1;
        }
      }
      else {
        receivedChars[ndx] = '\0'; // terminate the string
        recvInProgress = false;
        ndx = 0;
        newData = true;
      }
    }
    else if (rc == startMarker) {
      recvInProgress = true;
    }
  }
}

void parseData() {      // split the data into its parts

  char * strtokIndx; // this is used by strtok() as an index

  strtokIndx = strtok(tempChars,",");
  FLSpeed = atoi(strtokIndx);
 
  strtokIndx = strtok(NULL, ",");
  FRSpeed = atoi(strtokIndx);

  strtokIndx = strtok(NULL, ",");
  BLSpeed = atoi(strtokIndx);
  
  strtokIndx = strtok(NULL, ",");
  BRSpeed = atoi(strtokIndx); 

}

void setup() {
  Serial.begin(9600);
  // Set the maximum speed in steps per second:
  BLstepper.setMaxSpeed(MaxStepSpeed);
  BRstepper.setMaxSpeed(MaxStepSpeed);
  FLstepper.setMaxSpeed(MaxStepSpeed);
  FRstepper.setMaxSpeed(MaxStepSpeed);
  
  BLstepper.setAcceleration(StepAccel);
  BRstepper.setAcceleration(StepAccel);
  FLstepper.setAcceleration(StepAccel);
  FRstepper.setAcceleration(StepAccel);
  
}

void loop() {
  // Set the speed in steps per second:
  recvWithStartEndMarkers();
  if (newData == true) {
    strcpy(tempChars, receivedChars);
    parseData();
    newData = false;
  }
  sendSpeedsToSteppers();
  runSteppers();
}
