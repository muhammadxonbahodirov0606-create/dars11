tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

barcha = tadbir_1.intersection(tadbir_2, tadbir_3)
hammasi = tadbir_1 | tadbir_2 | tadbir_3

bitta = set()
ikkita = set()

for ism in hammasi:
    soni = (ism in tadbir_1) + (ism in tadbir_2) + (ism in tadbir_3)

    if soni == 1:
        bitta.add(ism)
    if soni >= 2:
        ikkita.add(ism)

print("Barcha tadbirlarda:", barcha)
print("Faqat bitta tadbirda:", bitta)
print("Kamida ikkita tadbirda:", ikkita)