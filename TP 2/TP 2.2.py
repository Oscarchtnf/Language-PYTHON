print("Quelle est votre Taille en m ?")
Taille = input()
print("Quelle est votre Poids en kg ?")
Poids = input()
Taille = float (Taille)
Poids = float (Poids)

IMC = Poids/(Taille*Taille)
print(IMC)
if IMC >=25:
    print("Vous devriez surveiller votre alimentation")
elif IMC <=19:
    print("Vous devriez prendre des forces")
else :
    print("Vous etes a votre poids de forme")