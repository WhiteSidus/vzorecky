while True:

    print ("Vitejte v programu")

    print ("Pro vypočet objemu zadejte 1")
    print ("Pro vypočet obvod zadejte 2")
    print ("Pro vypočet objemu zadejte 3")
    print ("Pro ukončení zadejte 4.")

    volba = input()
    pokracovani = True

    if volba == "1":
        print ("Zadejte v decimetrech")
        a = int(input("Zadejte stanu A: "))
        b = int(input("Zadejte stanu B: "))
        c = int(input("Zadejte stanu C: "))

        if a>0 and b>0 and c>0:
            vysledek = a*b*c
            print("Objem kvadru je: ", vysledek, " litr")
        else:
            print("Co delaš!? Je to chyba -_-")

    elif volba == "2":
        a = int(input("Zadejte stanu A: "))
        b = int(input("Zadejte stanu B: "))
        if a>0 and b>0:
            vysledek = 2*a+2*b
            print("Obvod kvadru je: ", vysledek)

        else:
            print("Co delaš!? Je to chyba -_-")

    elif volba == "3":
        print("Pro vypočet obsahu zadávejte delku strany v CM")
        a = int(input("Zadejte stanu A: "))
        b = int(input("Zadejte stanu B: "))

        if a>0 and b>0:
                vysledek = 2*a+2*b
            
                print("Obvod kvadru je: ", vysledek, " cm/2")
        else:
            print("Co delaš!? Je to chyba -_-")
    
    elif volba == "4":
        print("Ukončení programů!")
        break

    else:
        print("Zadal něco špantě nebo vubec ne zadal")
