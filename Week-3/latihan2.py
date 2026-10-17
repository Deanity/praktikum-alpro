# Latihan 2: Kondisi Batas (Off-by-One Error & Perbaikan Batas)
# Modul Praktikum 3 - Pola Perulangan

n = int(input("Jumlah 1 sampai n, n = "))
total = 0
i = 1

# Menggunakan i <= n agar batas atas (n) ikut dijumlahkan
while i <= n:
    total = total + i
    i = i + 1

print("Jumlah:", total)
