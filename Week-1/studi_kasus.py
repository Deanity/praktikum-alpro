# Studi Kasus — Program Cek Kelulusan Mahasiswa
# Modul Praktikum 1: Variabel, Tipe Data, dan Percabangan (if-else)

nama = input("Masukkan nama mahasiswa: ")
nilai = int(input("Masukkan nilai akhir (0-100): "))

# 1. Cek Kelulusan Sesuai Tabel Studi Kasus
if nilai >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"{nama} dengan nilai akhir {nilai} dinyatakan {status}")

# 2. Tantangan Tambahan (Opsional): Kategori Nilai Huruf (A/B/C/D)
if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")
