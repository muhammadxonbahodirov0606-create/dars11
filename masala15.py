import csv
import matplotlib.pyplot as plt

fayl = "kitoblar.csv"

def korish():
    with open(fayl) as f:
        print(list(csv.DictReader(f)))

def qidirish():
    nom = input("Nom: ")
    with open(fayl) as f:
        for k in csv.DictReader(f):
            if nom.lower() in k["nom"].lower():
                print(k)

def filtrlash():
    tur = input("Kategoriya: ")
    with open(fayl) as f:
        for k in csv.DictReader(f):
            if k["kategoriya"].strip() == tur:
                print(k)

def eng_kop():
    with open(fayl) as f:
        k = max(csv.DictReader(f), key=lambda x: int(x["oqilgan"]))
        print(k["nom"], k["oqilgan"])

def grafik():
    with open(fayl) as f:
        k = list(csv.DictReader(f))
    plt.bar([x["nom"] for x in k], [int(x["oqilgan"]) for x in k])
    plt.show()

def qoshish():
    with open(fayl, "a", newline="") as f:
        csv.writer(f).writerow([input("Nom: "), input("Tur: "), input("Muallif: "), input("O'qilgan: ")])

while True:
    t = input("1.Ko'rish 2.Qidirish 3.Filtrlash 4.Eng ko'p 5.Grafik 6.Qo'shish 0.Chiqish: ")
    if t == "1": korish()
    elif t == "2": qidirish()
    elif t == "3": filtrlash()
    elif t == "4": eng_kop()
    elif t == "5": grafik()
    elif t == "6": qoshish()
    elif t == "0": break