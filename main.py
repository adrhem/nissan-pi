#!/usr/bin/env python
import serial
import time

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
    print tag
  time.sleep(.01)
