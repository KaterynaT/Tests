from PIL import Image, ImageFont, ImageDraw

im = Image.new('RGB', (200,200), (0,0,255))
dr = ImageDraw.Draw(im)

# use a bitmap font
# font = ImageFont.load("arial.ttf")

dr.text((10, 10), "hello")

# use a truetype font
font = ImageFont.truetype("arial.ttf", 20)

dr.text((10, 25), "world", font=font)
im.save("text.png")
