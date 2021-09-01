import time
import picamera
import numpy as np
from PIL import Image, ImageDraw
from sys import version_info as vi

# Create an array representing a 800x480 image of
# a cross through the center of the display. The shape of
# the array must be of the form (height, width, color)
a = np.zeros((480, 800, 3), dtype=np.uint8)
a[240, 200:600, :] = 0xff
a[40:440, 400, :] = 0xff

i = Image.fromarray(a)
draw = ImageDraw.Draw(i)
draw.ellipse((300, 140, 500, 340), outline ='white')
b = np.asarray(i)

def getbuffer(b):
    return np.getbuffer(b) if vi.major<3 else b.tobytes()

camera = picamera.PiCamera()
# camera.resolution = (1280, 720)
# camera.framerate = 24
# camera.start_preview()
# Add the overlay directly into layer 3 with transparency;
# we can omit the size parameter of add_overlay as the
# size is the same as the camera's resolution
o = camera.add_overlay(getbuffer(b), layer=3, alpha=128)
# camera.stop_preview()
try:
    # Wait indefinitely until the user terminates the script
    while True:
        time.sleep(1)
finally:
    camera.remove_overlay(o)
