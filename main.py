#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()

import os
import serial
import time
import requests

api_url = os.getenv("API_URL")
antenna_id = os.getenv("ANTENNA_ID")

ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate = 38400,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

prev = ''
while 1:
  ser.write("\x0A\x55\x0D")

  tag = ser.read(ser.inWaiting()).replace("U","").replace("X","").strip()
  if tag != prev and tag != '':
    prev = tag
    url = "%slog" % api_url
    data = {'tag': tag, 'location': antenna_id} 
    res = requests.post(url, data)
  time.sleep(.01)
