tertinggi = None
urutan_tertinggi = None
banyak_diatas_80 = 0
total_diatas_80 = 0

for i in range(1, 9):
    suhu = int(input(f"Suhu pencatatan ke-{i}: "))
    
    if tertinggi is None or suhu > tertinggi:
        tertinggi = suhu
        urutan_tertinggi = i
        
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
