import random as r

bet = float(input("Add meg a kívánt tétet! "))
elso_dontes = r.choice(["fekete", "piros"])
valasz1 = input("Piros vagy Fekete? ")

if (elso_dontes == "piros") and (valasz1.lower() == "piros"):
    elso_dontes1 = r.randint(2, 11)
    print(f"A téted jelenlegi értéke: {bet * 2}")
    print(f"A lap színe és értéke: piros, {elso_dontes1}")
    valasz2 = input("A következő lap kisebb vagy nagyobb értékű? ")
    uj_lap = r.randint(2, 11)
    if (valasz2.lower() == "kisebb") and (uj_lap < elso_dontes1):
        print(f"A téted jelenlegi értéke: {bet * 3}")
        print(f"Az első lap színe és értéke: piros, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")

        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztetél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap > elso_dontes1):
        print(f"A téted jelenlegi értéke: {bet * 3}")
        print(f"Az első lap színe és értéke: piros, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be!")
    elif ((valasz2.lower() == "nagyobb") or (valasz2.lower() == "kisebb")) and (
        uj_lap == elso_dontes1
    ):
        print("Vesztettél!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap < elso_dontes1):
        print("Vesztettél!")
    elif (valasz2.lower() == "kisebb") and (uj_lap > elso_dontes1):
        print("Vesztettél!")


elif (elso_dontes == "fekete") and (valasz1.lower() == "fekete"):
    elso_dontes1 = r.randint(2, 11)
    print(f"A téted jelenlegi értéke: {bet * 2}")
    print(f"A lap színe és értéke: fekete, {elso_dontes1}")
    valasz2 = input("A következő lap kisebb vagy nagyobb értékű? ")
    uj_lap = r.randint(2, 11)
    if (valasz2.lower() == "kisebb") and (uj_lap < elso_dontes1):
        print(f"A téted jelenlegi értéke: {bet * 3}")
        print(f"Az első lap színe és értéke: fekete, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")

        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztetél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap > elso_dontes1):
        print(f"A téted jelenlegi értéke: {bet * 3}")
        print(f"Az első lap színe és értéke: fekete, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            print(f"A téted jelenlegi értéke: {bet * 4}")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if szimbolum == valasz4:
                print("Profi vagy!")
                print(f"A téted végső értéke: {bet * 20}")
            else:
                print("Vesztettél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be!")
    elif ((valasz2.lower() == "nagyobb") or (valasz2.lower() == "kisebb")) and (
        uj_lap == elso_dontes1
    ):
        print("Vesztettél!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap < elso_dontes1):
        print("Vesztettél!")
    elif (valasz2.lower() == "kisebb") and (uj_lap > elso_dontes1):
        print("Vesztettél!")
