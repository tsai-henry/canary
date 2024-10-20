#include <SoftwareSerial.h>

void setup()
{
    Serial.begin(9600); // monitor
    // no Serial1
}
 void loop()
{   
    float voltage;
    float temp;
    voltage = analogRead(0); // A0
    temp = (500 * voltage) / 1024;
    Serial.println(temp);
    delay(1000);
}