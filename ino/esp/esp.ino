#include <ESP8266WiFi.h>
#include <WiFiServer.h>
#include <SoftwareSerial.h>

// Access Point credentials
const char* ssid = "esp";
const char* password = "esp";

// port 8080
WiFiServer server(8080);

SoftwareSerial arduinoSerial(13, 14); // rx on pin 13

void setup() {
  Serial.begin(9600);   // monitor
  arduinoSerial.begin(9600);

  // esp softap
  Serial.println(WiFi.softAP(ssid));

  Serial.print("ESP8266 IP Address: ");
  Serial.println(WiFi.softAPIP());

  server.begin();
  Serial.println("Server started!");
}

void loop() {
  Serial.println("Looking for clients...");
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("Client connected!");

    // send data if connected
    while (client.connected()) {
      Serial.println(arduinoSerial.available());
      if (arduinoSerial.available() > 0) {
        String temp = arduinoSerial.readStringUntil('\n');
        Serial.println(temp);
        client.print(temp);
      }
      else {
        Serial.println("Serial is not available");
      }
      delay(1000);
    }

    client.stop();
    Serial.println("Client disconnected.");
  }
  delay(1000);
}