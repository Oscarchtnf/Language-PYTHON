Taille = input("Quelle est votre Taille en m ?")
Poids = input("Quelle est votre Poids en kg ?")
Genre = input("Quelle est votre Genre ( H ou F)?")
Taille = float (Taille)
Poids = float (Poids)
Genre =int=(Genre)


IMC = Poids/(Taille*Taille)
print(IMC)

if Genre =="H": #c un homme
    if IMC >=25:
        print("Vous devriez surveiller votre alimentation")
    else :
        if IMC <=19:
            print("Vous devriez prendre des forces")
        else :
            print("Vous etes a votre poids de forme")

else :#c'est une femme
        if IMC >=23:
            print("Vous devriez surveiller votre alimentation")
        else :
            if IMC <=18:
                print("Vous devriez prendre des forces")
            else :
                print("Vous etes a votre poids de forme")