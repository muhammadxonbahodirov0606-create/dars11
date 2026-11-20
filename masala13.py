import csv

yonalish = input("Yo'nalish: ")
talabalar = []

with open("talabalar.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        if qator["yonalish"] == yonalish:
            talabalar.append(qator)

talabalar.sort(key=lambda talaba: int(talaba["ball"]), reverse=True)

with open("filtrlangan_talabalar.csv", "w", newline="") as fayl:
    yozish = csv.DictWriter(fayl, fieldnames=["ism", "yosh", "yonalish", "ball"])
    yozish.writeheader()
    yozish.writerows(talabalar)

print(f"{len(talabalar)} ta talaba topildi. Natijalar filtrlangan_talabalar.csv fayliga yozildi.")