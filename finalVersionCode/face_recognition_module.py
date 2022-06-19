import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
# from gpiozero import Servo
from time import sleep
from rpi_lcd import LCD
import pigpio

pins = [27, 17, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

# SERVO setting
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


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/myproject/trainer/trainer_jjinbob.yml')

cascadePath = "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

names = ['Soyeon', 'joy', 'Sarah', 'paper', 'bob', 'W']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1)  # Flip vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.8,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            if (confidence < 50 and confidence < 100):
                led_on('G')
                lcd.text("welcome", 1)
                open()
                lcd.clear()

            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            led_on('R')
            lcd.text("get out", 1)
            sleep(2)
            lcd.clear()

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()