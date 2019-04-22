from PIL import Image
import colorsys

'''V1: coverting image to grayscale'''
img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

def convert_rgb_grayscale():
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i,j]

            y = (0.299 * r + 0.587 * g + 0.114 * b)
            pixels[i, j] = (int(round(y)), int(round(y)), int(round(y)))

    img.show()
convert_rgb_grayscale()

'''V2 coverting image to grayscale'''

def convert_hsv_func():
    for i in range(width):
        for j in range(height):
            # colorsys uses colors in the range [0, 1]
            r,g,b = pixels[i,j]

            hue, saturation, value = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            # do some math on h, s, v

            hue += 0.8
            saturation += 0.5
            value += 0.2

            r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

            # convert back to [0, 255]

            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

    img.show()
convert_hsv_func()

