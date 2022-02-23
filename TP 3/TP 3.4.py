x =735
tentatives = 0
while True:
    nbr =int(input("Saisir un nombre"))
    tentatives=tentatives+1
    if nbr>x:
        print("trop grand")
    elif nbr<x:
        print("trop petit")
    else :
        print("bravo Vous avez gangné en ",tentatives,"de tentatives")
    if nbr==x:
        break
    if tentatives >9:
        print("vous avez échoué")
        break
        