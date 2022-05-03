from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

#create the in-memory stream
stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2);
camera.capture(stream, format='jpeg')
camera.stop_preview()

#"Rewind" the stream to the beginning so we can read its content
stream.seek(0)
image = Image.open(stream)