skaitli = [5, 2, 8, 1, 4]

print(f"Sākotnējais saraksts: {skaitli}")

n = len(skaitli)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if skaitli[j] > skaitli[j + 1]:
            # maiņa vietām
            skaitli[j], skaitli[j + 1] = skaitli[j + 1], skaitli[j]

    print(f"Pēc {i + 1}. ārējā cikla: {skaitli}")

print(f"Sakārtots saraksts: {skaitli}")