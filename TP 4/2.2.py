from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")
for loop in range(800):
    im.putpixel((loop,250),(0,0,0))
im.show()