#define led 3
#include<cvzone.h>
SerialData serialData(1,3);

int valRecv[1];
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  serialData.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valRecv);
  analogWrite(led,map(valRecv[0],0,100,0,255));
  delay(1);
}
