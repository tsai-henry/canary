#include <SoftwareSerial.h>

void setup()
{
    Serial.begin(9600); // monitor
    Serial1.begin(9600); // rx tx
}
 void loop()
{   
    float voltage;
    float temp;
    voltage = analogRead(0); // A0
    temp = (500 * voltage) / 1024;
    Serial.println(temp);
    Serial1.println(temp);
    delay(1000);
}