import time
from picamera.renderers import PiOverlayRenderer
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

renderer = PiOverlayRenderer(None, getbuffer(b), resolution=(800,480), fullscreen=True, layer=3, alpha=128)

try:
    # Wait indefinitely until the user terminates the script
    while True:
        time.sleep(1)
finally:
    print("done") # camera.remove_overlay(o)
