import random as r

elso_dontes = r.choice(["fekete", "piros"])
valasz1 = input("Piros vagy Fekete? ")

if (elso_dontes == "piros") and (valasz1.lower() == "piros"):
    elso_dontes1 = r.randint(2, 11)
    print(f"A lap színe és értéke: piros, {elso_dontes1}")
    valasz2 = input("A következő lap kisebb vagy nagyobb értékű? ")
    uj_lap = r.randint(2, 11)
    if (valasz2.lower() == "kisebb") and (uj_lap < elso_dontes1):
        print(f"Az első lap színe és értéke: piros, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if (
                ((szimbolum == "rombusz") and (valasz4 == "rombusz"))
                or ((szimbolum == "lóhere") and (valasz4 == "lóhere"))
                or ((szimbolum == "szív") and (valasz4 == "szív"))
                or ((szimbolum == "levél") and (valasz4 == "levél"))
            ):
                print("Profi vagy!")
            else:
                print("Vesztettél!")

        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if (
                ((szimbolum == "rombusz") and (valasz4 == "rombusz"))
                or ((szimbolum == "lóhere") and (valasz4 == "lóhere"))
                or ((szimbolum == "szív") and (valasz4 == "szív"))
                or ((szimbolum == "levél") and (valasz4 == "levél"))
            ):
                print("Profi vagy!")
            else:
                print("Vesztetél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap > elso_dontes1):
        print(f"Az első lap színe és értéke: piros, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
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


if (elso_dontes == "fekete") and (valasz1.lower() == "fekete"):
    elso_dontes1 = r.randint(2, 11)
    print(f"A lap színe és értéke: fekete, {elso_dontes1}")
    valasz2 = input("A következő lap kisebb vagy nagyobb értékű? ")
    uj_lap = r.randint(2, 11)
    if (valasz2.lower() == "kisebb") and (uj_lap < elso_dontes1):
        print(f"Az első lap színe és értéke: fekete, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if (
                ((szimbolum == "rombusz") and (valasz4 == "rombusz"))
                or ((szimbolum == "lóhere") and (valasz4 == "lóhere"))
                or ((szimbolum == "szív") and (valasz4 == "szív"))
                or ((szimbolum == "levél") and (valasz4 == "levél"))
            ):
                print("Profi vagy!")
            else:
                print("Vesztettél!")

        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
            szimbolum = r.choice(["rombusz", "lóhere", "szív", "levél"])
            valasz4 = input(
                "Milyen szimbólumú a következő lap (rombusz, lóhere, szív, levél)? "
            )
            if (
                ((szimbolum == "rombusz") and (valasz4 == "rombusz"))
                or ((szimbolum == "lóhere") and (valasz4 == "lóhere"))
                or ((szimbolum == "szív") and (valasz4 == "szív"))
                or ((szimbolum == "levél") and (valasz4 == "levél"))
            ):
                print("Profi vagy!")
            else:
                print("Vesztettél!")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél csicska vagy!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél csicska vagy!")
        else:
            print("Rosszat írtál be")
    elif (valasz2.lower() == "nagyobb") and (uj_lap > elso_dontes1):
        print(f"Az első lap színe és értéke: piros, {elso_dontes1}")
        print(f"Az új lap értéke: {uj_lap}")
        valasz3 = input("A következő lap értéke az első kettő között vagy nem? (i/n) ")
        uj_lap1 = r.randint(2, 11)
        if (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Helyes")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Helyes")
        elif (uj_lap1 in range(uj_lap, elso_dontes1)) and (valasz3 == "n"):
            print("Vesztettél!")
        elif (uj_lap1 not in range(uj_lap, elso_dontes1)) and (valasz3 == "i"):
            print("Vesztettél!")
        else:
            print("Rosszat írtál be")
    elif ((valasz2.lower() == "nagyobb") or (valasz2.lower() == "kisebb")) and (
        uj_lap == elso_dontes1
    ):
        print("Vesztettél!")
    elif (valasz2.lower() == "nagyobb") and (uj_lap < elso_dontes1):
        print("Vesztettél!")
    elif (valasz2.lower() == "kisebb") and (uj_lap > elso_dontes1):
        print("Vesztettél!")
