from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")
for loop in range(600):
    im.putpixel((250,loop),(0,0,0))
im.show()