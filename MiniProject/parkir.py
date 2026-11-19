# ==================== TAHAP 1: Konstanta & Tabel Tarif ====================
TARIF_MOTOR_PERTAMA = 2000
TARIF_MOTOR_BERIKUTNYA = 1000
TARIF_MOTOR_MAKSIMUM = 8000
TARIF_MOBIL_PERTAMA = 4000
TARIF_MOBIL_BERIKUTNYA = 2000
TARIF_MOBIL_MAKSIMUM = 16000

BATAS_GRATIS_MENIT = 15
PERSEN_DISKON = 20
PERSEN_PENUH = 100
DENDA_TIKET_HILANG = 10000
PENANDA_SELESAI = "SELESAI"

MENIT_PER_JAM = 60
JAM_TERBESAR = 23
MENIT_TERBESAR = 59
JAM_TABEL_MULAI = 1
JAM_TABEL_AKHIR = 8

print("===== PARKIRKU KAMPUS SURABAYA =====")
print("Tabel Tarif:")
print("Jam | Motor | Mobil")
for jam in range(JAM_TABEL_MULAI, JAM_TABEL_AKHIR + 1):
    tarif_motor_tabel = TARIF_MOTOR_PERTAMA + (jam - 1) * TARIF_MOTOR_BERIKUTNYA
    if tarif_motor_tabel > TARIF_MOTOR_MAKSIMUM:
        tarif_motor_tabel = TARIF_MOTOR_MAKSIMUM
    tarif_mobil_tabel = TARIF_MOBIL_PERTAMA + (jam - 1) * TARIF_MOBIL_BERIKUTNYA
    if tarif_mobil_tabel > TARIF_MOBIL_MAKSIMUM:
        tarif_mobil_tabel = TARIF_MOBIL_MAKSIMUM
    print(jam, "  | Rp", tarif_motor_tabel, "| Rp", tarif_mobil_tabel)
print()

# Variabel rekap (nilai awal)
jumlah_kendaraan = 0
jumlah_motor = 0
jumlah_mobil = 0
jumlah_gratis = 0
jumlah_diskon = 0
jumlah_denda = 0
total_pendapatan = 0
durasi_terlama = 0
plat_terlama = ""
bayar_tertinggi = 0
plat_bayar_tertinggi = ""

# TAHAP 4: Perulangan Berpenanda
plat = input("Plat nomor (ketik SELESAI untuk berhenti): ")

while plat != PENANDA_SELESAI:

    # TAHAP 2: Masukan & Validasi 
    jenis = input("Jenis kendaraan (motor/mobil): ")
    while jenis != "motor" and jenis != "mobil":
        print("Jenis harus motor atau mobil.")
        jenis = input("Jenis kendaraan (motor/mobil): ")

    # Waktu masuk
    sah = False
    while not sah:
        jam_masuk = int(input("Jam masuk (0-23): "))
        menit_masuk = int(input("Menit masuk (0-59): "))
        if (jam_masuk >= 0 and jam_masuk <= JAM_TERBESAR
                and menit_masuk >= 0 and menit_masuk <= MENIT_TERBESAR):
            sah = True
        else:
            print("Waktu tidak valid.")
    waktu_masuk = jam_masuk * MENIT_PER_JAM + menit_masuk

    # Waktu keluar (tidak boleh sebelum waktu masuk)
    sah = False
    while not sah:
        jam_keluar = int(input("Jam keluar (0-23): "))
        menit_keluar = int(input("Menit keluar (0-59): "))
        waktu_keluar = jam_keluar * MENIT_PER_JAM + menit_keluar
        if not (jam_keluar >= 0 and jam_keluar <= JAM_TERBESAR
                and menit_keluar >= 0 and menit_keluar <= MENIT_TERBESAR):
            print("Waktu tidak valid.")
        elif waktu_keluar < waktu_masuk:
            print("Waktu keluar tidak boleh sebelum waktu masuk.")
        else:
            sah = True

    kartu = input("Punya kartu civitas? (ya/tidak): ")
    while kartu != "ya" and kartu != "tidak":
        print("Jawaban harus ya atau tidak.")
        kartu = input("Punya kartu civitas? (ya/tidak): ")

    tiket_hilang = input("Tiket hilang? (ya/tidak): ")
    while tiket_hilang != "ya" and tiket_hilang != "tidak":
        print("Jawaban harus ya atau tidak.")
        tiket_hilang = input("Tiket hilang? (ya/tidak): ")

    # TAHAP 3: Hitung Biaya & Struk
    durasi = waktu_keluar - waktu_masuk
    jam_ditagih = (durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM

    if durasi <= BATAS_GRATIS_MENIT:
        tarif_dasar = 0
    elif jenis == "motor":
        tarif_dasar = TARIF_MOTOR_PERTAMA + (jam_ditagih - 1) * TARIF_MOTOR_BERIKUTNYA
        if tarif_dasar > TARIF_MOTOR_MAKSIMUM:
            tarif_dasar = TARIF_MOTOR_MAKSIMUM
    else:
        tarif_dasar = TARIF_MOBIL_PERTAMA + (jam_ditagih - 1) * TARIF_MOBIL_BERIKUTNYA
        if tarif_dasar > TARIF_MOBIL_MAKSIMUM:
            tarif_dasar = TARIF_MOBIL_MAKSIMUM

    if kartu == "ya" and not tiket_hilang == "ya" and tarif_dasar > 0:
        diskon = tarif_dasar * PERSEN_DISKON // PERSEN_PENUH
    else:
        diskon = 0

    if tiket_hilang == "ya":
        denda = DENDA_TIKET_HILANG
    else:
        denda = 0

    total = tarif_dasar - diskon + denda

    print()
    print("--- STRUK", plat, "---")
    print("Jenis       :", jenis)
    print("Durasi      :", durasi // MENIT_PER_JAM, "jam", durasi % MENIT_PER_JAM, "menit")
    print("Jam ditagih :", jam_ditagih)
    print("Tarif dasar : Rp", tarif_dasar)
    print("Diskon      : Rp", diskon)
    print("Denda       : Rp", denda)
    print("TOTAL       : Rp", total)
    print()

    # Perbarui data rekap
    jumlah_kendaraan = jumlah_kendaraan + 1
    if jenis == "motor":
        jumlah_motor = jumlah_motor + 1
    else:
        jumlah_mobil = jumlah_mobil + 1
    if tarif_dasar == 0:
        jumlah_gratis = jumlah_gratis + 1
    if diskon > 0:
        jumlah_diskon = jumlah_diskon + 1
    if denda > 0:
        jumlah_denda = jumlah_denda + 1
    total_pendapatan = total_pendapatan + total
    if durasi > durasi_terlama:  # strict ">" : bila seri, yang lebih dulu tetap
        durasi_terlama = durasi
        plat_terlama = plat
    if total > bayar_tertinggi:
        bayar_tertinggi = total
        plat_bayar_tertinggi = plat

    # Baca plat berikutnya di akhir blok
    plat = input("Plat nomor (ketik SELESAI untuk berhenti): ")

# TAHAP 5: Rekap Akhir
print()
print("===== REKAP PARKIR HARI INI =====")
if jumlah_kendaraan == 0:
    print("Belum ada kendaraan yang tercatat.")
else:
    rata_rata = total_pendapatan // jumlah_kendaraan
    print("Jumlah kendaraan   :", jumlah_kendaraan)
    print("  Motor            :", jumlah_motor)
    print("  Mobil            :", jumlah_mobil)
    print("Parkir gratis      :", jumlah_gratis)
    print("Mendapat diskon    :", jumlah_diskon)
    print("Kena denda tiket   :", jumlah_denda)
    print("Total pendapatan   : Rp", total_pendapatan)
    print("Rata-rata/kendaraan: Rp", rata_rata)
    print("Parkir terlama     :", plat_terlama, "(", durasi_terlama // MENIT_PER_JAM,
          "jam", durasi_terlama % MENIT_PER_JAM, "menit )")
    print("Bayar tertinggi    :", plat_bayar_tertinggi( "( Rp", bayar_tertinggi, ")"))
    print("Grafik jumlah kendaraan:")
    batang_motor = ""
    for i in range(jumlah_motor):
        batang_motor = batang_motor + "#"
    batang_mobil = ""
    for i in range(jumlah_mobil):
        batang_mobil = batang_mobil + "#"
    print("Motor |", batang_motor)
    print("Mobil |", batang_mobil)