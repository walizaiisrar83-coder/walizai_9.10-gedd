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
        mazakais = None
        lielakais = None

        for i in range(1, skaits + 1):
            ievade2 = input(f"Ievadi {i}. skaitli: ").strip()

            if ievade2 == "" or not ievade2.lstrip("-").isdigit():
                print("Kļūda: lūdzu ievadi veselu skaitli!")
                break
            else:
                skaitlis = int(ievade2)

                if mazakais is None or skaitlis < mazakais:
                    mazakais = skaitlis
                if lielakais is None or skaitlis > lielakais:
                    lielakais = skaitlis
        else:
            print(f"Mazākais skaitlis: {mazakais}")
            print(f"Lielākais skaitlis: {lielakais}")