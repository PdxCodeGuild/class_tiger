"""
Lab16: Image Manipulation
"""
from PIL import Image, ImageDraw
from random import randint

def stick_figure():
    width = 1000
    height = 1000

    img = Image.new('RGB',(width,height))

    draw = ImageDraw.Draw(img)

    # the origin (0,0) is at the top left corner

    draw.rectangle(((0,0),(width,height)),fill="white")

    # draw a rect from x0, y0,x1,y1

    # draw.rectangle(((100,100),(300,300)), fill = "black")

    #draw a line from x0,y0, x1, y1

    color = (256,128,128) # pink
    # draw.line((0,0,(width/2),0),fill = 'red')
    draw.line((300,height,500,700),fill = 'black')
    draw.line((700,height,500,700),fill = 'black')
    draw.line((500,700,500,200),fill = 'black')
    draw.line((500,450,250,250),fill = 'black')
    draw.line((500,450,750,250),fill = 'black')


    circle_x = 500
    circly_y = 200
    circle_radius =100
    draw.ellipse((circle_x - circle_radius, circly_y - circle_radius,circle_x+circle_radius,circly_y+circle_radius),fill='black')

    img.show()

stick_figure()

def gen_random():
    width = 500
    height = 500

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for i in range(1000):
        x0 = randint(0, width)
        y0 = randint(0, height)
        x1 = randint(0, width)
        y1 = randint(0, height)
        line_width = randint(1, 40)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

    img.show()


gen_random()
