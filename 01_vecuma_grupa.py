ievade = input("Ievadi savu vecumu:").strip()
try:
    if ievade == "":
        print("Kļūda: ievade ir tukša!")
    else:
        vecums = int(ievade)

        if vecums < 0:
            print("Kļūda: vecums nevar būt negatīvs!")
        elif vecums <= 12:
            print("bērns")
        elif vecums <= 17:
            print("pusaudzis")
        elif vecums <= 64:
            print("pieaugušais")
        else:
            print("seniors")
except ValueError:
    print('Klūda: ievade nav skaitlis!')