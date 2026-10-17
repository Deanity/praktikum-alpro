# Studi Kasus: Rekap Nilai Kuis Kelas
# Modul Praktikum 2: Percabangan Bertingkat dan Perulangan Dasar

total = 0
lulus = 0
remedial = 0
tidak_lulus = 0
tertinggi = 0
terendah = None

jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))

for i in range(1, jumlah_mahasiswa + 1):
    nilai = int(input(f"Nilai mahasiswa ke-{i}: "))
    
    # Validasi rentang nilai 0 - 100 dengan while loop
    while nilai < 0 or nilai > 100:
        print("Nilai harus 0-100, coba lagi")
        nilai = int(input(f"Nilai mahasiswa ke-{i}: "))
    
    # Percabangan bertingkat untuk kategori kelulusan
    if nilai >= 60:
        if nilai >= 85:
            kategori = "Lulus Sangat Baik"
        else:
            kategori = "Lulus"
        lulus += 1
    else:
        if nilai >= 40:
            kategori = "Remedial"
            remedial += 1
        else:
            kategori = "Tidak Lulus"
            tidak_lulus += 1
            
    print(f"Kategori: {kategori}")
    
    # Akumulasi nilai dan pencarian nilai tertinggi & terendah
    total += nilai
    if nilai > tertinggi:
        tertinggi = nilai
    if terendah is None or nilai < terendah:
        terendah = nilai

# Rekap Akhir Kelas
rata_rata = total / jumlah_mahasiswa if jumlah_mahasiswa > 0 else 0

print("\n=== REKAP KUIS ===")
print(f"Rata-rata   : {rata_rata:.1f}")
print(f"Tertinggi   : {tertinggi}")
if terendah is not None:
    print(f"Terendah    : {terendah}")
print(f"Lulus       : {lulus}")
print(f"Remedial    : {remedial}")
print(f"Tidak lulus : {tidak_lulus}")
