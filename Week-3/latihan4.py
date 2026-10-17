# Latihan 4: Pola Akumulator dan Pencacah
# Modul Praktikum 3 - Pola Perulangan

TARGET = 50
HARI = 10

total = 0
di_bawah = 0

for hari in range(1, HARI + 1):
    produksi = int(input(f"Produksi hari ke-{hari}: "))
    total = total + produksi
    if produksi < TARGET:
        di_bawah = di_bawah + 1

print("Total produksi:", total)
print("Rata-rata per hari:", total / HARI)
print("Hari di bawah target:", di_bawah)
