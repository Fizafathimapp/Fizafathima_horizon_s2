#include <Servo.h>

Servo myServo;

int potPin = A0;
int ledPin = 7;

int potValue;
int angle;

void setup() {
  myServo.attach(9);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  potValue = analogRead(potPin);

  // Map potentiometer (0–1023) to angle (0–180)
  angle = map(potValue, 0, 1023, 0, 180);

  if (angle > 68) {
    angle = 68;              // Limit to 68 degrees
    digitalWrite(ledPin, LOW);  // Turn LED OFF
  } else {
    digitalWrite(ledPin, HIGH);   // Turn LED ON
  }

  myServo.write(angle);

  delay(15);
}