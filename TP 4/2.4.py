from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")
    
for y in range(600):
    for x in range(0,800,60):
        im.putpixel((x,y),(0,0,255))
im.show()