import csv

kategoriyalar = {}

with open("savdo.csv", "r") as fayl:
    malumot = csv.DictReader(fayl)

    for qator in malumot:
        kategoriya = qator["kategoriya"]
        narx = int(qator["narx"])
        miqdor = int(qator["miqdor"])

        tushum = narx * miqdor

        if kategoriya in kategoriyalar:
            kategoriyalar[kategoriya] += tushum
        else:
            kategoriyalar[kategoriya] = tushum

for kategoriya, tushum in kategoriyalar.items():
    print(f"{kategoriya}: {tushum:,} so'm")

eng_daromadli = max(kategoriyalar, key=kategoriyalar.get)

print("Eng daromadli kategoriya:", eng_daromadli)