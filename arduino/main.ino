void setup() {
   Serial.begin(9600); // begin transmission
}
void loop() {
  String val;
  while (Serial.available() > 0) {
    val = val + (char)Serial.readStringUntil('\n'); // read data byte by byte and store it
  }
  Serial.print("Received: " + val); // send the received data back to raspberry pi
}