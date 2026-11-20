import csv

talabalar = [
    ["Madina", 18, "Python", 95],
    ["Aziza", 19, "Python", 88],
    ["Malika", 19, "Python", 79]
]

with open("filtrlangan_talabalar.csv", "w", newline="") as fayl:
    yozish = csv.writer(fayl)

    yozish.writerow(["ism", "yosh", "yonalish", "ball"])
    yozish.writerows(talabalar)

print("Ma'lumotlar faylga yozildi.")