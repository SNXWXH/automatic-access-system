import serial
import RPi.GPIO as GPIO
from serial import Serial
from time import sleep
from rpi_lcd import LCD
import pigpio

ser = Serial('/dev/ttyACM0', 9600)

# RGB LED setting
pins = [27, 17, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

pi1 = pigpio.pi()
pi2 = pigpio.pi()

# LCD setting
lcd = LCD()


# RGB LED def
def led_on(rgb):
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.LOW)
    sleep(0.2)
    if rgb == "R":
        GPIO.output(pins[0], GPIO.HIGH)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.output(pins[2], GPIO.LOW)
        sleep(2)
        GPIO.output(pins[0], GPIO.LOW)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.output(pins[2], GPIO.LOW)
        sleep(0.2)

    if rgb == "G":
        GPIO.output(pins[0], GPIO.HIGH)
        GPIO.output(pins[1], GPIO.HIGH)
        GPIO.output(pins[2], GPIO.LOW)
        sleep(2)
        GPIO.output(pins[0], GPIO.LOW)
        GPIO.output(pins[1], GPIO.LOW)
        GPIO.output(pins[2], GPIO.LOW)
        sleep(0.2)


# SERVO def
def open():
    pi1.set_servo_pulsewidth(16, 0)
    pi2.set_servo_pulsewidth(13, 0)
    sleep(1)
    pi1.set_servo_pulsewidth(16, 500)
    pi2.set_servo_pulsewidth(13, 500)
    sleep(1)
    pi1.set_servo_pulsewidth(16, 1500)
    pi2.set_servo_pulsewidth(13, 1500)
    sleep(1)
    pi1.set_servo_pulsewidth(16, 500)
    pi2.set_servo_pulsewidth(13, 500)
    sleep(1)


while True:
    if ser.readable():
        res = ser.readline()
        num = int(res.decode()[:len(res) - 1])
        if (num == 1):
            led_on('G')
            lcd.text("welcome", 1)
            open()
            lcd.clear()
        elif (num == 0):
            led_on('R')
            lcd.text("get out", 1)
            lcd.clear()
        elif (num == 2):
            led_on('G')
            lcd.text("hi jjini", 1)
            open()
            lcd.clear()
        elif (num == 3):
            led_on('G')
            lcd.text("hi 0l0jjo", 1)
            open()
            lcd.clear()
        elif (num == 4):
            led_on('G')
            lcd.text("hi bboggo", 1)
            open()
            lcd.clear()
        elif (num == 5):
            led_on('G')
            lcd.text("hi 17__apr", 1)
            open()
            lcd.clear()
        elif (num == 6):
            led_on('R')
            lcd.text("get out", 1)
            sleep(2)
            lcd.clear()