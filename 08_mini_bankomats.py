atlikums = 100.0

while True:
    print()
    print("=== Mini bankomāts ===")
    print("1 — apskatīt atlikumu")
    print("2 — iemaksāt naudu")
    print("3 — izņemt naudu")
    print("4 — beigt darbu")

    izvele = input("Izvēlies darbību (1-4): ").strip()

    if izvele == "1":
        print(f"Pašreizējais atlikums: {atlikums:.2f} EUR")

    elif izvele == "2":
        summa_teksts = input("Ievadi iemaksas summu: ").strip()

        if summa_teksts == "" or not summa_teksts.replace(".", "", 1).lstrip("-").isdigit():
            print("Kļūda: lūdzu ievadi derīgu skaitli!")
        else:
            summa = float(summa_teksts)
            if summa <= 0:
                print("Kļūda: summai jābūt lielākai par 0!")
            else:
                atlikums += summa
                print(f"Iemaksāts {summa:.2f} EUR. Jaunais atlikums: {atlikums:.2f} EUR")

    elif izvele == "3":
        summa_teksts = input("Ievadi izņemamo summu: ").strip()

        if summa_teksts == "" or not summa_teksts.replace(".", "", 1).lstrip("-").isdigit():
            print("Kļūda: lūdzu ievadi derīgu skaitli!")
        else:
            summa = float(summa_teksts)
            if summa <= 0:
                print("Kļūda: summai jābūt lielākai par 0!")
            elif summa > atlikums:
                print(f"Kļūda: nepietiek līdzekļu! Pieejamais atlikums: {atlikums:.2f} EUR")
            else:
                atlikums -= summa
                print(f"Izņemts {summa:.2f} EUR. Jaunais atlikums: {atlikums:.2f} EUR")

    elif izvele == "4":
        print("Darbs pabeigts. Uz redzēšanos!")
        break

    else:
        print("Kļūda: nederīga izvēlne! Lūdzu izvēlies 1, 2, 3 vai 4.")