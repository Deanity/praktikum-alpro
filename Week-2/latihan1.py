# Latihan 1: Percabangan Bertingkat
# Modul Praktikum 2: Percabangan Bertingkat dan Perulangan Dasar

umur = int(input("Masukkan umur: "))
kartu_pelajar = input("Punya kartu pelajar? (ya/tidak): ")

if umur >= 17:
    print("Umur memenuhi syarat nonton film 17+")
    if kartu_pelajar == "ya":
        print("Tiket: harga pelajar Rp30000")
    else:
        print("Tiket: harga umum Rp45000")
else:
    print("Maaf, film ini khusus usia 17 tahun ke atas")
