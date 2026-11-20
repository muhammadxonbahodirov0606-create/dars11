matn = "Hamma bilan bir hil bolish mening uslubim emas."

sozlar = matn.lower().replace(".", "").split()

print("So'zlar soni:", len(sozlar))

eng_uzun = max(sozlar, key=len)
print("Eng uzun so'z:", eng_uzun)

harflar = matn.lower().replace(" ", "").replace(".", "")

eng_kop = max(set(harflar), key=harflar.count)
print("Eng ko'p uchragan harf:", eng_kop)

takrorlanmagan = []

for soz in sozlar:
    if sozlar.count(soz) == 1:
        takrorlanmagan.append(soz)

print("Takrorlanmaydigan so'zlar:", ", ".join(takrorlanmagan))