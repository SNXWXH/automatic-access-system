import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
camera.rotation = 180
camera.start_preview()
camera.annotate_text = 'Thank you, Sarah ~ ^8^ '
time.sleep(2)

#take a picture including the annotation
camera.capture('foo.jpg')
camera.stop_preview()