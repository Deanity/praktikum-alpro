# Latihan 3: Perulangan while
# Modul Praktikum 2: Percabangan Bertingkat dan Perulangan Dasar

total = 0
angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    total = total + angka
    angka = int(input("Masukkan angka (0 untuk berhenti): "))

print("Total semua angka:", total)
