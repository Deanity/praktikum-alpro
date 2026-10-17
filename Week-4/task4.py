# Task 4 - Rekap Produksi Harian Lini Perakitan (Studi Kasus Modul 3)

TARGET = 100
PENANDA = -1

banyak_hari = 0
total_produksi = 0
hari_target = 0
total_target = 0

tertinggi = None
hari_tertinggi = None
terendah = None
hari_terendah = None

produksi = int(input("Produksi hari ke-1 (-1 untuk selesai): "))

while produksi != PENANDA:
    banyak_hari += 1
    total_produksi += produksi
    
    if banyak_hari == 1:
        tertinggi = produksi
        hari_tertinggi = 1
        terendah = produksi
        hari_terendah = 1
    else:
        if produksi > tertinggi:
            tertinggi = produksi
            hari_tertinggi = banyak_hari
        if produksi < terendah:
            terendah = produksi
            hari_terendah = banyak_hari
            
    if produksi >= TARGET:
        hari_target += 1
        total_target += produksi
        
    produksi = int(input(f"Produksi hari ke-{banyak_hari + 1} (-1 untuk selesai): "))

print("\n=== REKAP PRODUKSI ===")
if banyak_hari == 0:
    print("Belum ada data produksi.")
else:
    rata_rata = total_produksi / banyak_hari
    print(f"Banyak hari            : {banyak_hari}")
    print(f"Total produksi         : {total_produksi}")
    print(f"Rata-rata per hari     : {rata_rata:.2f}")
    print(f"Hari mencapai target ({TARGET}): {hari_target}")
    print(f"Tertinggi: {tertinggi} unit (hari ke-{hari_tertinggi})")
    print(f"Terendah : {terendah} unit (hari ke-{hari_terendah})")
    
    if hari_target > 0:
        rata_target = total_target / hari_target
        print(f"Rata-rata hari target  : {rata_target:.2f}")
