#
# Simple weather data logger
#

import schedule
import time
from serial import Serial

portname = '/dev/ttyUSB0'  # portname = 'COM1' on Windows
portspeed = 9600
logfilename = 'weather-log.txt'
station_name = 'ABC'       # should be unique

def log_data():
    log_time = time.asctime()
    serial = Serial(portname, portspeed, timeout=None)
    time.sleep(3)  # wait for Arduino to reset
    serial.write(b'F')
    response = serial.readline().decode('utf-8')
    print(station_id, log_time, response.rstrip())
    with open(logfilename, 'a') as f:
        f.write(station_id * log_time + ',' + response)
    
    
log_data() # do once on startup
schedule.every(5).minutes.do(log_data)

while True:
    schedule.run_pending()
    time.sleep(1)
