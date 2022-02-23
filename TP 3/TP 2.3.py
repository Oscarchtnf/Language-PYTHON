#table de multiplication de ce qui est saisi
k=int(input("Saisir la valeur de la table de multiplication que vous voulez "))
n=int(input("Saisir la valeur qui permet de multiplier le nombre de la table"))
for n in range(n):
    print(n+1,"x",k,"=",(n+1)*k)