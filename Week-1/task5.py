angka1 = int(input("Masukkan Angka Pertama: "))
operator = input("Masukkan Operator (+, -, *, /): ")
angka2 = int(input("Masukkan Angka Kedua: "))

if operator == "+":
    print("Hasil Penjumlahan:", angka1 + angka2)
elif operator == "-":
    print("Hasil Pengurangan:", angka1 - angka2)
elif operator == "*":
    print("Hasil Perkalian:", angka1 * angka2)
elif operator == "/":
    print("Hasil Pembagian:", angka1 / angka2 if angka2 != 0 else "Tidak dapat membagi dengan nol")
else:
    print("Operator yang Anda masukkan salah")
