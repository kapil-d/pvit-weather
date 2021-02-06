#
# Simple weather data logger
#
import  sys
import schedule
import time
import requests
from serial import Serial

portname = '/dev/ttyUSB0'  # portname = 'COM1' on Windows
portspeed = 9600
logfilename = 'weather-log.txt'
server_url = None

# Process command line arguments
if len(sys.argv) < 2:
    print("Please specify a station id.")
    exit()
    
station_id=sys.argv[1]

if len(sys.argv) > 2:
    server_url = sys.argv[2]
    
# Log the data    
def log_data():
    log_time = time.asctime()
    serial = Serial(portname, portspeed, timeout=None)
    time.sleep(3)  # wait for Arduino to reset
    serial.write(b'F')
    response = serial.readline().decode('utf-8')
    temperature = round(float(response), 1)
    with open(logfilename, 'a') as f:
        f.write(station_id + ',' + log_time + ',' + str(temperature) + '\n')

    # Log to server if server address was specified
    if server_url != None:
        payload = {'station': station_id, 'datetime': log_time,
                   'temp': temperature}
        r = requests.post("http://{}/submit".format(server_url), params=payload)

    # print message
    print(station_id, log_time, temperature, end=' ')
    if server_url != None:
        print("sent to {}".format(server_url), end='')
    print() # newline

log_data() # do once on startup
schedule.every(5).minutes.do(log_data)

while True:
    schedule.run_pending()
    time.sleep(1)
