print ("Vítejte v aplikaci pro výpočet obdelníku")
a = int(input("Zadejte délku strany A: "))
b = int(input("Zadejte délku strany B: "))
if a>0 and b>0:
    print("Výsledek je: ")
    print(2*a+2*b)
else: 
    print ("Chyba")

