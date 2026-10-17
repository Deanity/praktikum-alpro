# Latihan 3: Masukan Berpenanda (Sentinel) dan Penanganan Data Kosong
# Modul Praktikum 3 - Pola Perulangan

total = 0
banyak = 0

durasi = int(input("Waktu proses (menit, -1 selesai): "))

while durasi != -1:
    total = total + durasi
    banyak = banyak + 1
    durasi = int(input("Waktu proses (menit, -1 selesai): "))

if banyak == 0:
    print("Belum ada data yang dimasukkan.")
else:
    print("Banyak data:", banyak)
    print("Rata-rata:", round(total / banyak, 2), "menit")
