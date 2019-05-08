from PIL import Image
# import math
img = Image.open("Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

import colorsys


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h = h + .6
        s = s - s * .5
        v = v - .3
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pixels[i, j] = (r, g, b)


img.show()