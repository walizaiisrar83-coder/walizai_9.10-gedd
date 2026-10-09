ievade = input("Cik skaitļus ievadīsi? ").strip()

if ievade == "":
    print("Kļūda: ievade ir tukša!")
elif not ievade.lstrip("-").isdigit():
    print("Kļūda: lūdzu ievadi veselu skaitli!")
else:
    skaits = int(ievade)

    if skaits <= 0:
        print("Kļūda: skaitļu skaitam jābūt pozitīvam (lielākam par 0)!")
    else:
        summa = 0
        pozitivo = 0
        negativo = 0
        nulles = 0
        para = 0
        nepаra = 0
        derigi = 0

        for i in range(1, skaits + 1):
            ievade2 = input(f"Ievadi {i}. skaitli: ").strip()

            if ievade2 == "" or not ievade2.lstrip("-").isdigit():
                print("Kļūda: lūdzu ievadi veselu skaitli! Šis skaitlis tiks izlaists.")
                continue

            skaitlis = int(ievade2)
            derigi += 1

            summa += skaitlis

            if skaitlis > 0:
                pozitivo += 1
            elif skaitlis < 0:
                negativo += 1
            else:
                nulles += 1

            if skaitlis % 2 == 0:
                para += 1
            else:
                nepаra += 1

        print()
        print("=== Rezultāti ===")

        if derigi == 0:
            print("Netika ievadīts neviens derīgs skaitlis.")
        else:
            videjais = summa / derigi
            print(f"Summa: {summa}")
            print(f"Pozitīvie: {pozitivo}")
            print(f"Negatīvie: {negativo}")
            print(f"Nulles: {nulles}")
            print(f"Pāra skaitļi: {para}")
            print(f"Nepāra skaitļi: {nepаra}")
            print(f"Vidējais aritmētiskais: {videjais}")