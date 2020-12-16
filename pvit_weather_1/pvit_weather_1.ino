#include <OneWire.h>
#include <DallasTemperature.h>
 
// Data wire is plugged into pin 2 on the Arduino
int one_wire_bus = 2;
 
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire my_oneWire(one_wire_bus);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&my_oneWire);
 
void setup(void)
{
  // start serial port
  Serial.begin(9600);

  // Start up the library
  sensors.begin();
}
 
 
void loop(void)
{
  // call sensors.requestTemperatures() to issue a global temperature
  // request to all devices on the bus
  if (Serial.available() > 0) {
    char command = Serial.read();
    while (Serial.available() > 0) {
      Serial.read();
    }
    sensors.requestTemperatures(); // Send the command to get temperatures
    if (command == 'C') {
      Serial.println(sensors.getTempCByIndex(0));
    }
    if (command == 'F') {
      Serial.println(sensors.getTempFByIndex(0));
    } 
  } 
    // You can have more than one IC on the same bus. 
    // 0 refers to the first IC on the wire
    delay(100);
}
