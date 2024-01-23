print ("Vítejte v aplikaci pro výpočet obsahu obdelnika")
#Deklarace proměnich a přetypovaní na str
a = int(input("Zadejte délku: "))
b = int(input("Zadejte šyrku: "))
#Kontrolujeme zaporne čislo
if a>0 and b>0:
    print("Výsledek je: ")
    print(a*b)
#Pokud nebude platit první podminka, splíse else
else: 
    print ("Chyba")