# Latihan 4 — Percabangan if-elif-else
# Modul Praktikum 1: Variabel, Tipe Data, dan Percabangan (if-else)

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
