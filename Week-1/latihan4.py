nilai = int(input("Masukkan nilai ujian (0-100): "))

if nilai >= 85:
    kategori = "A"
elif nilai >= 70:
    kategori = "B"
elif nilai >= 55:
    kategori = "C"
else:
    kategori = "D"

print("Kategori nilai kamu:", kategori)
