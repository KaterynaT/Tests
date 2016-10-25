"""
Using the PIL(pilllow) Python library, draw the scroll box showing the value,
on which it is moved left or right(from 0 to 100).  Make the
runner ellipsoid, so that it would better fit the box.
"""

from PIL import Image, ImageFont, ImageDraw


def draw_little_rect(scroll):
    im = Image.open("slider_00.jpg")
    dr = ImageDraw.Draw(im)

    if scroll <= 100:
        size = (480*(scroll-5.5)/100)
    else:
        size = (480*(100-5.5))/100
    color = (96, 10, 0)
    x1 = 145 + size
    x2 = 180 + size
    # dr.rectangle(((base_x,39),(x,20)), fill=color)
    dr.ellipse((x1,20, x2,39), fill='blue', outline='blue')
    font = ImageFont.truetype("fonts/Arial Narrow Bold Italic.ttf", 11)
    dr.text((154+size, 23), str(scroll), fill=color, font=font)
    im.save("rectangle.png")

draw_little_rect(10)

