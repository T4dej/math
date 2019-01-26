# -*- coding: utf-8 -*-

def sestevanje():
    p = 0  # seštevanje pravilnih odgovorov
    n = 0  # seštevanje nepravilnih odgovorov
    print("Reši naloge seštevanja.")
    for y in range(1, 11):
        import random
        num1 = random.randint(1,101)
        num2 = random.randint(1,100 - num1) #zagotovimo z drugo spremenljivko, da ne gremo z seštevanjem preko števila 100

        print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
        print(str(num1) + " + " + str(num2) + " = ")

        while True:
            try:
                rez = int(input("Ogovor: \n"))
                if rez == num1 + num2:
                    print("ODLIČNO!! Odgovor je pravilen!\n")
                    p = p + 1 #sešteva pravilne odgovore
                    break
                else:
                    print("Žal, nepravilno!\n")
                    n = n + 1
                    break
            except ValueError:
                print("Vnesi celo številko.")

    print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
    vprasanje = input("Ali želiš ponoviti nalogo seštevanja? (da/ne)")
    if vprasanje == "da":
        sestevanje()
    else:
        print("Hvala za reševanje.\n")

def odstevanje():
    p = 0  # seštevanje pravilnih odgovorov
    n = 0  # seštevanje nepravilnih odgovorov
    print("Reši naloge odštevanja.")

    for y in range(1, 11):
        import random
        num1 = random.randint(1,101)
        num2 = random.randint(1,num1) #z drugo vrednostjo določimo max številko, ki ne sme presegati prve

        print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
        print(str(num1) + " - " + str(num2) + " = ")

        while True:
            try:
                rez = int(input("Ogovor: \n"))
                if rez == num1 - num2:
                    print("ODLIČNO!! Odgovor je pravilen!\n")
                    p = p + 1 #sešteva pravilne odgovore
                    break
                else:
                    print("Žal, nepravilno!\n")
                    n = n + 1
                    break
            except ValueError:
                print("Vnesi celo številko.")

    print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
    vprasanje = input("Ali želiš ponoviti nalogo odštevanja? (da/ne)")
    if vprasanje == "da":
        odstevanje()
    else:
        print("Hvala za reševanje.\n")

def mnozenje():
    p = 0  # seštevanje pravilnih odgovorov
    n = 0  # seštevanje nepravilnih odgovorov
    print("Reši naloge množenja.")

    for y in range(1, 11):
        import random
        num1 = random.randint(1,10)
        num2 = random.randint(1,10) #z drugo vrednostjo določimo max številko, ki ne sme presegati prve

        print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
        print(str(num1) + " X " + str(num2) + " = ")

        while True:
            try:
                rez = int(input("Ogovor: \n"))
                if rez == num1 * num2:
                    print("ODLIČNO!! Odgovor je pravilen!\n")
                    p = p + 1 #sešteva pravilne odgovore
                    break
                else:
                    print("Žal, nepravilno!\n")
                    n = n + 1
                    break
            except ValueError:
                print("Vnesi celo številko.")

    print("Rezultat        Pravilni: " + str(p) + "       Nepravilni: " + str(n))
    vprasanje = input("Ali želiš ponoviti nalogo množenja? (da/ne)")
    if vprasanje == "da":
        mnozenje()
    else:
        print("Hvala za reševanje.\n")



print("Pozdravljen/a v programu za matematiko.\n")
while True:
    try:
        izbira = int(input(" Za seštevanje pritisni 1\n Za odštevanje pritisni 2\n Za množenje pritisni 3\n Za izhod pritisni 5\n"))
        if izbira == 1:
            sestevanje()
        elif izbira == 2:
            odstevanje()
        elif izbira == 3:
            mnozenje()
        elif izbira == 5:
            print("Želim ti lep dan.")
            input("Pritisni ENTER za izhod")
            quit()
    except ValueError:
        print("Izberi število od 1 do 5\n")



