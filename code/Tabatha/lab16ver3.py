from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height), "white")

draw = ImageDraw.Draw(img)

circle_x = 250
circle_y = 150
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
draw.line((250, 190, 250, 300), fill='lightgreen', width = 4)
draw.line((190, 225, 310, 225), fill='lightgreen', width = 4)
draw.line((250, 300, 310, 355), fill='lightgreen', width = 4)
draw.line((250, 300, 190, 355), fill='lightgreen', width = 4)
circle_x = 310
circle_y = 205
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='pink')
draw.polygon([310, 245, 300, 205, 320, 205], fill ="tan")

img.show()