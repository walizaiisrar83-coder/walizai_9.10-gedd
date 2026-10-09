skaitli = [4, 7, 2, 9, 7, 1]

ievade = input("Ievadi meklējamo skaitli: ").strip()

if ievade == "":
    print("Kļūda: ievade ir tukša!")
elif not ievade.lstrip("-").isdigit():
    print("Kļūda: lūdzu ievadi veselu skaitli!")
else:
    meklejamais = int(ievade)

    pirmais_indekss = -1
    visi_indeksi = []

    for i in range(len(skaitli)):
        if skaitli[i] == meklejamais:
            if pirmais_indekss == -1:
                pirmais_indekss = i
            visi_indeksi.append(i)

    if pirmais_indekss == -1:
        print("Nav atrasts")
    else:
        print(f"Pirmais indekss: {pirmais_indekss}")
        print(f"Visi indeksi: {visi_indeksi}")