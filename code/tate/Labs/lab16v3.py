"""
Lab16: Image Manipulation
"""
from PIL import Image, ImageDraw


width = 500
height = 500

img = Image.new('RGB',(width,height))

draw = ImageDraw.Draw(img)

# the origin (0,0) is at the top left corner

draw.rectangle(((0,0),(width,height)),fill="white")

# draw a rect from x0, y0,x1,y1

# draw.rectangle(((100,100),(300,300)), fill = "black")

#draw a line from x0,y0, x1, y1

color = (256,128,128) # pink
draw.line((0,0,width,height),fill = 'black')
draw.line((0,height,width,0),fill = 'black')

circle_x = width/2
circly_y = height/2
circle_radius =100
draw.ellipse((circle_x - circle_radius, circly_y - circle_radius,circle_x+circle_radius,circly_y+circle_radius),fill='lightgreen')




img.show()
