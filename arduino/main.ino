#include <AccelStepper.h>

const int FL_STEP_Pin = 5;
const int FL_DIR_Pin = 4;

const int FR_STEP_Pin = 3;
const int FR_DIR_Pin = 2;

const int BL_STEP_Pin = 9;
const int BL_DIR_Pin = 8;
  
const int BR_STEP_Pin = 6;
const int BR_DIR_Pin = 7;

const int stepperInterfaceType = 1;

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars]; 


int FLSpeed = 0;
int FRSpeed = 0;
int BLSpeed = 0;
int BRSpeed = 0;

AccelStepper FL_Stepper = AccelStepper(stepperInterfaceType, FL_STEP_Pin, FL_DIR_Pin);
AccelStepper FR_Stepper = AccelStepper(stepperInterfaceType, FR_STEP_Pin, FR_DIR_Pin);
AccelStepper BL_Stepper = AccelStepper(stepperInterfaceType, BL_STEP_Pin, BL_DIR_Pin);
AccelStepper BR_Stepper = AccelStepper(stepperInterfaceType, BR_STEP_Pin, BR_DIR_Pin);


boolean newData = false;

//============

void setup() {
    pinMode(FL_STEP_Pin, OUTPUT);
    pinMode(FL_DIR_Pin, OUTPUT);
  
    pinMode(FR_STEP_Pin, OUTPUT);
    pinMode(FR_DIR_Pin, OUTPUT);
  
    pinMode(BL_STEP_Pin, OUTPUT);
    pinMode(BL_DIR_Pin, OUTPUT);
  
    pinMode(BR_STEP_Pin, OUTPUT);
    pinMode(BR_DIR_Pin, OUTPUT);
  
    Serial.begin(9600);
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        //showParsedData();
        sendSpeedsToSteppers();
        runSteppers();
        newData = false;
    }
}

//============

void sendSpeedsToSteppers() {
    //Serial.println("Stepping");
    FL_Stepper.setSpeed(FLSpeed);
    FR_Stepper.setSpeed(FRSpeed);
    BL_Stepper.setSpeed(BLSpeed);
    BR_Stepper.setSpeed(BRSpeed);
}

void runSteppers() {
    //Serial.println("Running");
    FL_Stepper.runSpeed();
    FR_Stepper.runSpeed();
    BL_Stepper.runSpeed();
    BR_Stepper.runSpeed();
}

//============

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
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

//============

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

//============

void showParsedData() {
    Serial.print("FL: " + String(FLSpeed) + " | ");
    Serial.print("FR: " + String(FRSpeed) + " | ");
    Serial.print("BL: " + String(BLSpeed) + " | ");
    Serial.print("BR: " + String(BRSpeed) + "\n");
}