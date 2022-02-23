from PIL import Image
im = Image.new("RGB",(800,600),"lightgrey")


#fnction de tracé de ligne horizontale
def ligneH(y, couleur):
    for x in range(800):
        im.putpixel((x,y), couleur)
        
#Fonction de tracé de ligne verticale
def ligneV(x):
    for y in range(600):
        im.putixel((x, y), (0,0,0))
        
def carre(x0, y0, largeur, couleur):
    pass

#-------------prgrame principal---------