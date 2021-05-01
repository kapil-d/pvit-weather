//
// COMUNICATE WITH ESP8266 DEVICE - Simple Serial Passthru
//
// Use serial monitor to communicate with Arduino; Arduino passes Tx/Rx to ESP8266
//
// Pins: 2 - Arduino Rx to ESP8266 Tx
//       3 - Arduino Tx to ESP8266 Rx via voltage divider
//       Arduino Gnd to ESP8266 Gnd
//       Arduino 3.3V to ESP8266 Vcc
//       Pull CH_PD on ESP8266 HIGH to 3.3v with Pullup Resistor
//

#include <SoftwareSerial.h>

SoftwareSerial ESP8266Serial(2,3);   // 2:Rx, 3:Tx

void setup()
{
  Serial.begin(9600);
  
  ESP8266Serial.begin(115200);
  ESP8266Serial.println("AT+IPR=9600");
  delay(1000);
  ESP8266Serial.end();
  ESP8266Serial.begin(9600);

  Serial.println("Set NL and CR in Serial Monitor.");
  Serial.println("Ready.");
  Serial.println("");

}


void loop()
{
  if (ESP8266Serial.available()) {
    Serial.write(ESP8266Serial.read());
  }
  while (Serial.available()) {
    ESP8266Serial.write(Serial.read());
  }
}
