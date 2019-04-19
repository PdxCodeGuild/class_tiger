#image_manipulation.py
from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        

        Y = 0.299*R + 0.587*G + 0.114*B

        pixels[i, j] = (r, g, b)

img.show()
