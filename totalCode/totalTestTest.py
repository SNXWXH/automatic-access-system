import serial
import RPi.GPIO as GPIO
from serial import Serial
from gpiozero import Servo
from time import sleep
from rpi_lcd import LCD
 
ser = Serial('/dev/ttyACM0',9600)
 
#RGB LED setting
pins = [3, 2, 4]
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pins[0],GPIO.OUT)
GPIO.setup(pins[1],GPIO.OUT)
GPIO.setup(pins[2],GPIO.OUT)
 
#SERVO setting
servo1 = Servo(16)
servo2 = Servo(13)
servo1.value = 0
servo2.value = 0
 
#LCD setting
lcd = LCD()
 
#RGB LED def
def led_on(rgb):
    GPIO.output(pins[0],GPIO.LOW)
    GPIO.output(pins[1],GPIO.LOW)
    GPIO.output(pins[2],GPIO.LOW)
    sleep(0.2)
    if rgb == "R":
        GPIO.output(pins[0],GPIO.HIGH)
        GPIO.output(pins[1],GPIO.LOW)
        GPIO.output(pins[2],GPIO.LOW)
        sleep(0.2)
        
    if rgb == "G":
        GPIO.output(pins[0],GPIO.HIGH)
        GPIO.output(pins[1],GPIO.HIGH)
        GPIO.output(pins[2],GPIO.LOW)
        sleep(0.2)
 
#SERVO def
def open():
    servo1.value = 1
    servo2.value = -1
    sleep(3)
    servo1.value = -1
    servo2.value = 1
    sleep(1)
 
while True :
    if ser.readable() :
        res = ser.readline()
        num = int(res.decode()[:len(res)-1])
        if (num == 1):
            led_on('G')
            lcd.text("welcome",1)
            open()
        elif (num == 0):
            led_on('R')
            lcd.text("get out",1)
        elif (num == 2):
            led_on('G')
            lcd.text("hi jiini",1)
            open()
        elif (num == 3):
            led_on('G')
            lcd.text("hi jjung",1)
            open()
        elif (num == 4):
            led_on('G')
            lcd.text("hi mingzzi",1)
            open()
        elif (num == 5):
            led_on('G')
            lcd.text("hi sarah",1)
            open()
        elif (num == 6):
            led_on('R')
            lcd.text("you are not admin!",1)
            lcd.text("get out",2)