from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height), "white")

draw = ImageDraw.Draw(img)

circle_x = 250
circle_y = 150
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightblue')
draw.line((250, 190, 250, 300), fill='lightblue', width = 4)
draw.line((190, 225, 310, 225), fill='lightblue', width = 4)
draw.line((250, 300, 310, 355), fill='lightblue', width = 4)
draw.line((250, 300, 190, 355), fill='lightblue', width = 4)
circle_x = 265
circle_y = 145
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
circle_x = 235
circle_y = 145
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
draw.arc([235, 165, 265, 180], start = 0, end = 180, fill='blue', width=4)
circle_x = 310
circle_y = 187
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='pink')
circle_x = 310
circle_y = 200
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

draw.polygon([310, 245, 300, 205, 320, 205], fill ="tan")

img.show()