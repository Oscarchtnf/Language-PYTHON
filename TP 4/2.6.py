from PIL import Image



#fnction de tracé de ligne horizontale
def ligneH(y, couleur):
    for x in range(800):
        im.putpixel((x,y), couleur)
        
#Fonction de tracé de ligne verticale
def ligneV(x):
    for y in range(600):
        im.putpixel((x, y), (0,0,0))
        
def carre(x0, y0, largeur, couleur):
    for x in range (x0, x0+largeur):
        for y in range(y0, y0+largeur):
            im.putpixel((x, y), (couleur))

def rectangle(x0, y0, largeur,hauteur, couleur):
    for x in range (x0, x0+largeur):
        for y in range(y0, y0+hauteur):
            im.putpixel((x, y), (couleur))


#-------------prgrame principal---------
im = Image.new("RGB",(800,600),"white")


rectangle(0,600//2,800,300,(255,0,0))
for y in range(300):
    for x in range(y+1):
        im.putpixel((x, y),(0,0,255))

for y in range(300,600):
    for x in range(600-y):
        im.putpixel((x, y),(0,0,255))



im.show()