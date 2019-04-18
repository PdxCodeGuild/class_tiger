from PIL import Image
import math
img = Image.open("Lenna_(test_image).png")
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = 0.299 * r + 0.587 * g + 0.114 * b
        y = math.ceil(y)
        r = y
        g = y
        b = y
        pixels[i, j] = (r, g, b)

# def brightness(x):

img.show()