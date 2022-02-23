print("saisir la valeur du rayon")
rayon = input()
rayon=float(rayon)#transforme la chaine en nombre réel
PI = 3.14
surface = PI * rayon * rayon
circonference= 2 *PI * rayon
print("la surface du cercle de rayon" ,rayon, "vaut:" ,surface)
print("la circonference du cercle de rayon" ,rayon, "vaut:" ,circonference)