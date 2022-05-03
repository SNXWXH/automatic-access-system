from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.rotation = 180
sleep(5)
camera.stop_preview()
