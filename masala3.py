import math

shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}

eng_katta_masofa = 0
eng_uzoq_yonalish = ""

nomlar = list(shaharlar.keys())

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        shahar1 = nomlar[i]
        shahar2 = nomlar[j]

        x1, y1 = shaharlar[shahar1]
        x2, y2 = shaharlar[shahar2]

        masofa = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        print(shahar1, "va", shahar2, ":", masofa)

        if masofa > eng_katta_masofa:
            eng_katta_masofa = masofa
            eng_uzoq_yonalish = shahar1 + " — " + shahar2

print("Eng uzoq yo'nalish:", eng_uzoq_yonalish, "(", eng_katta_masofa, ")")