def nilai_valid(n):
    return 0 <= n <= 100


def baca_nilai(label):
    nilai = float(input(label))
    while not nilai_valid(nilai):
        print("Nilai harus 0 sampai 100.")
        nilai = float(input(label))
    return nilai


def nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)


def nilai_huruf(na):
    if na >= 85:
        return "A"
    elif na >= 70:
        return "B"
    elif na >= 55:
        return "C"
    else:
        return "D"


def rata_rata(total, banyak):
    if banyak == 0:
        return 0
    return total / banyak


# Program Utama
jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))
jumlah_lulus = 0
total_nilai = 0

for i in range(jumlah_mahasiswa):
    nama = input("Nama: ")
    tugas = baca_nilai("Nilai tugas: ")
    uts = baca_nilai("Nilai UTS: ")
    uas = baca_nilai("Nilai UAS: ")

    na = nilai_akhir(tugas, uts, uas)
    huruf = nilai_huruf(na)
    total_nilai += na

    if na >= 55:
        jumlah_lulus += 1

    print(f"{nama} -> NA: {round(na, 2)} | Huruf: {huruf}")

print(f"Jumlah lulus: {jumlah_lulus} dari {jumlah_mahasiswa}")
print(f"Rata-rata nilai akhir: {round(rata_rata(total_nilai, jumlah_mahasiswa), 2)}")
