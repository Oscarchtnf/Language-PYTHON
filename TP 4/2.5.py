from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")
    
for x in range(800):
    for y in range(0,600,60):
        im.putpixel((x,y),(0,255,0))
im.show()