ievade = input("Ievadi veselu pozitīvu skaitli n: ").strip()

if ievade == "":
    print("Kļūda: ievade ir tukša!")
elif not ievade.lstrip("-").isdigit():
    print("Kļūda: lūdzu ievadi veselu skaitli!")
else:
    n = int(ievade)

    if n <= 0:
        print("Kļūda: skaitlim jābūt pozitīvam (lielākam par 0)!")
    else:
        summa = 0
        for i in range(1, n + 1):
            summa += i
        print(f"Summa no 1 līdz {n} ir {summa}")