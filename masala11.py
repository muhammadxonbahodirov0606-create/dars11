import json

with open("sozlamalar.json", "r") as fayl:
    sozlamalar = json.load(fayl)

mavzu = input("Mavzu (light/dark): ")
bildirishnoma = input("Bildirishnoma (ha/yo'q): ")

sozlamalar["mavzu"] = mavzu

if bildirishnoma == "ha":
    sozlamalar["bildirishnoma"] = True
else:
    sozlamalar["bildirishnoma"] = False

with open("sozlamalar.json", "w") as fayl:
    json.dump(sozlamalar, fayl, indent=4)

print("Sozlamalar yangilandi.")