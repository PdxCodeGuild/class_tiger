from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

# draw.rectangle(((0, 0), (width, height)), fill="white")

# # draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# # draw a line from x0, y0, x1, y1
# # using the color pink


circle_x = 250
circle_y = 150
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

# color = (256, 128, 128)  # pink
draw.line((250, 190, 250, 300), fill='lightgreen', width = 4)
draw.line((190, 225, 310, 225), fill='lightgreen', width = 4)
draw.line((250, 300, 310, 355), fill='lightgreen', width = 4)
draw.line((250, 300, 190, 355), fill='lightgreen', width = 4)


img.show()