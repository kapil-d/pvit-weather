#
# Simple weather data logger
#

import schedule
import time
from serial import Serial

portname = '/dev/ttyUSB0'
portspeed = 9600
logfilename = 'weather-log.txt'

def log_data():
    log_time = time.asctime()
    serial = Serial(portname, portspeed, timeout=None)
    time.sleep(3)  # wait for Arduino to reset
    serial.write(b'F')
    response = serial.readline().decode('utf-8')
    print(log_time, response.rstrip())
    with open(logfilename, 'a') as f:
        f.write(log_time + ',' + response)
    
    
log_data() # do once on startup
schedule.every(5).minutes.do(log_data)

while True:
    schedule.run_pending()
    time.sleep(1)
