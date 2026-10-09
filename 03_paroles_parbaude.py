pareiza_parole = "skola2024"
meginajumi = 0
max_meginajumi = 3
piekluve = False

while meginajumi < max_meginajumi:
    parole = input("Ievadi paroli: ").strip()
    meginajumi += 1

    if parole == pareiza_parole:
        print("Piekļuve atļauta")
        piekluve = True
        break
    else:
        atlikusi = max_meginajumi - meginajumi
        if atlikusi > 0:
            print(f"Nepareiza parole! Atlikušie mēģinājumi: {atlikusi}")
        else:
            print("Nepareiza parole!")

if not piekluve:
    print("Piekļuve bloķēta")