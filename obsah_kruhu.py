print ("Vítejte v aplikaci pro výpočet obsahu kruhu")
#Deklarace proměnich a přetypovaní na str
a = str(input("Zadejte poloměr: "))
#Kontrolujeme zaporne čislo
if a>0:
    print("Výsledek je: ")
    print(3.14*(a*a))
#Pokud nebude platit první podminka, splíse else
else: 
    print ("Chyba")