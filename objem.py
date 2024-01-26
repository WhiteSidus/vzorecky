print ("Vítejte v aplikaci pro výpočet objemu")
#Deklarace proměnich a přetypovaní na str
a = int(input("Zadejte vyšku: "))
b = int(input("Zadejte šyrku: "))
c = int(input("Zadejte délku: "))
#Kontrolujeme zaporne čislo
if a>0 and b>0 and c>0:
    print("Výsledek je: ")
    print(a*b*c)
#Pokud nebude platit první podminka, splíse else
else: 
    print ("Chyba")