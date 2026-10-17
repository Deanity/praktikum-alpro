# Task 1 - Percabangan Bertingkat (Bioskop & Diskon Pelajar)

umur = int(input("Masukkan Umur : "))
kartu_pelajar = input("Apakah Memiliki Kartu Pelajar? (y/n) : ")

print("Umur Anda : ", umur)

if umur >= 17:
    print("Anda Boleh Menonton Bioskop")
    if kartu_pelajar.lower() == "y":
        print("Anda Mendapatkan Diskon Pelajar")
    else:
        print("Anda Tidak Mendapatkan Diskon Pelajar")
else:
    print("Anda Tidak Boleh Menonton Bioskop")
