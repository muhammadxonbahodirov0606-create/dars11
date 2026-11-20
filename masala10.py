jami_soat = 0
eng_kop = 0
eng_kop_ishlagan = ""

with open("ish_vaqti.txt", "r") as fayl:
    malumot = fayl.read().split()

for i in range(0, len(malumot), 2):
    ism = malumot[i]
    try:
        soat = int(malumot[i + 1])
        jami_soat += soat

        if soat > eng_kop:
            eng_kop = soat
            eng_kop_ishlagan = ism

    except ValueError:
        print(f"Ogohlantirish: {ism} uchun soat qiymati noto'g'ri.")

print("Jami ish soati:", jami_soat)
print(f"Eng ko'p ishlagan: {eng_kop_ishlagan} — {eng_kop} soat")