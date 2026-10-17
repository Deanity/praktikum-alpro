nama = input("Masukkan nama mahasiswa: ")
nilai = int(input("Masukkan nilai akhir (0-100): "))

if nilai >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"{nama} dengan nilai akhir {nilai} dinyatakan {status}")

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")
