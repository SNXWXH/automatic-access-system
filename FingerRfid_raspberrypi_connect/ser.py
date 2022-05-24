import serial
from serial import Serial

ser = Serial('/dev/ttyACM0',115200)

while True :
    if ser.readable() :
        res = ser.readline()
        print(res.decode()[:len(res)-1])