#admin1_capture.py

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text = 'Please wait for 30 seconds'
for i in range(5):
    sleep(5);
    camera.capture('admin1_%s.jpg' %i)
camera.stop_preview()