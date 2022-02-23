facto = 1
while True:
    n= int(input("Tapezla valeur de n :"))
    if n==0:
        break
    facto = 1
    for i in range(1,n+1):
        facto = facto  * i
    print("factorielle de n ", n,"est : ", facto)