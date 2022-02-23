print("Saisir la valeur de la Largeur")
Largeur = input()
hauteurM = input("Saisir la hauteur de la maison ?")
hauteurToit = input(" Saisir la hauteur du Toit ?")
longueurM = input("Saisir la valeur de la longueur de la maison ?")
Largeur = float (Largeur)
hauteurM = float (hauteurM)
hauteurToit = float (hauteurToit)
longueurM = float (longueurM)


KGdecrépisparmetrecarré = 1.5
Airedesdeuxcotés = (KGdecrépisparmetrecarré *(longueurM *(hauteurM-hauteurToit)))*2
print("Quantité de crépis sur les deux cotés de la maison :",Airedesdeuxcotés)

KGdecrépisparmetrecarré = 1.5
Airedesdeuxfacades = (KGdecrépisparmetrecarré *(Largeur*(hauteurM-hauteurToit)+(Largeur*hauteurToit)/2))*2
print("Quantité de crépis sur les deux facades de la maison :",Airedesdeuxfacades)


Surfacetotale = Airedesdeuxfacades + Airedesdeuxcotés
print("Quantité de crépis sur le toute la maison :",Surfacetotale)