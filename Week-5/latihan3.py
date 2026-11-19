def nilaimahasiswa(n):
    if n >= 85:
        print("A")
    elif n >= 75:
        print("AB")
    elif n >= 65:
        print("B")
    elif n >= 55:
        print("BC")
    elif n > 50:
        print("C")
    else:
        return "D"

def kelulusan(n):
    return n >= 60

for i in range(3):
    nilai = int(input("Masukkan Nilai: "))

    if kelulusan(nilai):
        status = "Lulus"
    else: 
        status = "Tidak Lulus"
    print(f"Nilai: {nilai} | Huruf: {nilaimahasiswa(nilai)} | Status: {status}")