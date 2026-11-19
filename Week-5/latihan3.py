def nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    return "D"


def lulus(nilai):
    return nilai >= 55


for i in range(3):
    n = int(input("Nilai: "))
    if lulus(n):
        status = "Lulus"
    else:
        status = "Tidak lulus"
    print(n, "->", nilai_huruf(n), "|", status)
