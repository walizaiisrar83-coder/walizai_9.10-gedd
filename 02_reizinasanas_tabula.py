ievade = input("Ievadi veselu skaitli: ").strip()

if ievade == "":
    print("Kļūda: ievade ir tukša!")
elif not ievade.lstrip("-").isdigit():
    print("Kļūda: lūdzu ievadi veselu skaitli!")
else:
    skaitlis = int(ievade)

    for i in range(1, 11):
        print(f"{skaitlis} x {i} = {skaitlis * i}")