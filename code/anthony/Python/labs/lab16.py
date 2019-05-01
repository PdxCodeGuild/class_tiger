from PIL import Image, ImageDraw
import colorsys
from random import randint

# Version 1
# img = Image.open("./text_files/lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
# 
# for i in range(width):
    # for j in range(height):
        # r, g, b = pixels[i, j]
# 
        # y = round(.299*r + .587*g + .114*b)
# 
        # pixels[i, j] = (y, y, y)
# 
# img.show()


# Version 2
# img = Image.open("./text_files/lenna.png")
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
        
#         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

#         s = 0

#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)
        
 
#         pixels[i, j] = (r, g, b)

# img.show()


width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((200, 200), (300, 400)), fill="lightblue")
draw.rectangle(((100, 200), (400, 250)), fill="lightblue")
draw.rectangle(((200, 400), (225, 500)), fill="lightblue")
draw.rectangle(((275, 400), (300, 500)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)


circle_x = width/2 
circle_y = height/2 - 100
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()

# width = 500
# height = 500
# 
# img = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(img)
# 
# for i in range(1000):
    # x0 = randint(0, width)
    # y0 = randint(0, height)
    # x1 = randint(0, width)
    # y1 = randint(0, height)
    # line_width = randint(1, 40)
    # red = randint(0, 255)
    # green = randint(0, 255)
    # blue = randint(0, 255)
    # draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)
# 
# img.show()