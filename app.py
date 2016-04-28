import serial
import time
import requests

ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

def send_reading(reading):
  line = "moisture,plant=money_tree value={}".format(reading)
  params = {"db": "oscar"}
  r = requests.post("http://192.168.1.140:8086/write", params=params, data=line, timeout=2.0)
  r.raise_for_status()

while True:
  line = ser.readline()
  if line:
    line = line.strip()
    
  if line:
    print "Got line: {}".format(line)
    send_reading(line)
