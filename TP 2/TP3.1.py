print("Quelle est la forme géométrique de l'aire que vous voulez calculer") 
print("R = Rectangle")
print("T = Triangle")
print("C = Cercle")
print("A = Carré")
Forme = input("Vous avez choisi la forme géométrique :")




if Forme == "T":
    print("Saisir la valeur de la base")
    base = input()
    hauteur = input("Saisir la hauteur ?")

    base = float (base)
    hauteur = float (hauteur)
    aire = base * hauteur /2
    print("Aire : ",aire)
    
elif Forme == "R":
    longueur = input("Saisir la valeur de la longueur")
    longueur = float (longueur)
    largeur = input("Saisir la valeur de la largeur")
    largeur = float(largeur)
    aire = largeur * longueur
    print("Aire : ",aire)
    
elif Forme == "A":
    Coté = input("Saisir la valeur des cotés")
    Coté = float (Coté)
    aire = Coté * Coté
    print("Aire : ",aire)
    
elif Forme == "C":
    print("saisir la valeur du rayon")
    rayon = input()
    rayon=float(rayon)#transforme la chaine en nombre réel
    PI = 3.14
    aire = PI * rayon * rayon
    print("L'Aire du cercle de rayon" ,rayon, "vaut:" ,aire)