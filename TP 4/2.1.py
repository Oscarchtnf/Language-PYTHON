from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")
im.putpixel((200,100),(0,0,0))
im.putpixel((500,200),(0,0,0))
im.putpixel((600,500),(0,0,0))
im.putpixel((700,400),(0,0,0))
im.show()


