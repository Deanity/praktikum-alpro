# Latihan 3: Mengelompokkan Masalah (Pencatatan Suhu Mesin)
# Modul Praktikum 3 (Latihan 7)

# Komentar Perancangan:
# - Sub-masalah 1: Suhu tertinggi beserta urutan (Pola Nilai Ekstrem: tertinggi, urutan_tertinggi)
# - Sub-masalah 2: Berapa kali suhu melebihi 80 derajat (Pola Pencacah: banyak_diatas_80 = 0)
# - Sub-masalah 3: Rata-rata suhu yang melebihi 80 derajat (Pola Akumulator & Pencacah: total_diatas_80 = 0)

tertinggi = None
urutan_tertinggi = None
banyak_diatas_80 = 0
total_diatas_80 = 0

for i in range(1, 9):
    suhu = int(input(f"Suhu pencatatan ke-{i}: "))
    
    # 1. Nilai Ekstrem
    if tertinggi is None or suhu > tertinggi:
        tertinggi = suhu
        urutan_tertinggi = i
        
    # 2. Penyaringan (> 80)
    if suhu > 80:
        banyak_diatas_80 += 1
        total_diatas_80 += suhu

print(f"Suhu tertinggi: {tertinggi} (pencatatan ke-{urutan_tertinggi})")

if banyak_diatas_80 == 0:
    print("Tidak ada suhu yang melebihi 80")
else:
    print(f"Suhu melebihi 80: {banyak_diatas_80} kali")
    rata_rata = total_diatas_80 / banyak_diatas_80
    print(f"Rata-rata suhu yang melebihi 80: {rata_rata:.2f}")
