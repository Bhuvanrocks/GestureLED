/*
 * Author: Bhuvan Kumar
 * GitHub: Bhuvanrocks
 * Description: Code to receive data from Serial , and map the value to the brightness of LED
 *
 * This code is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
 * You may obtain a copy of the license at https://creativecommons.org/licenses/by-sa/4.0/legalcode
 */

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
