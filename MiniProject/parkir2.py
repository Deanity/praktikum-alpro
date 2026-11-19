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
MENIT_PER_HARI = 24 * 60
JAM_TERBESAR = 23
MENIT_TERBESAR = 59
JAM_TABEL_MULAI = 1
JAM_TABEL_AKHIR = 8

print("===== PARKIRKU KAMPUS SURABAYA =====")
print("Tabel Tarif Harian:")
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

# Rekap per hari keluar
# Format: { hari: { ...rekap data... } }
rekap_harian = {}
hari_berjalan = 1

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
        if (0 <= jam_masuk <= JAM_TERBESAR and 0 <= menit_masuk <= MENIT_TERBESAR):
            sah = True
        else:
            print("Waktu tidak valid.")
    waktu_masuk = jam_masuk * MENIT_PER_JAM + menit_masuk

    # Waktu keluar (jika lebih kecil dari masuk, otomatis deteksi lewat tengah malam/nginap)
    sah = False
    while not sah:
        jam_keluar = int(input("Jam keluar (0-23): "))
        menit_keluar = int(input("Menit keluar (0-59): "))
        if 0 <= jam_keluar <= JAM_TERBESAR and 0 <= menit_keluar <= MENIT_TERBESAR:
            sah = True
        else:
            print("Waktu tidak valid.")
    waktu_keluar = jam_keluar * MENIT_PER_JAM + menit_keluar

    # Deteksi menginap & penentuan hari keluar
    if waktu_keluar >= waktu_masuk:
        menginap = False
        hari_keluar = hari_berjalan
        durasi = waktu_keluar - waktu_masuk
    else:
        menginap = True
        hari_keluar = hari_berjalan + 1
        durasi = (MENIT_PER_HARI - waktu_masuk) + waktu_keluar

    kartu = input("Punya kartu civitas? (ya/tidak): ")
    while kartu != "ya" and kartu != "tidak":
        print("Jawaban harus ya atau tidak.")
        kartu = input("Punya kartu civitas? (ya/tidak): ")

    tiket_hilang = input("Tiket hilang? (ya/tidak): ")
    while tiket_hilang != "ya" and tiket_hilang != "tidak":
        print("Jawaban harus ya atau tidak.")
        tiket_hilang = input("Tiket hilang? (ya/tidak): ")

    # TAHAP 3: Hitung Biaya & Struk
    jam_ditagih = (durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM
    tarif_maks = TARIF_MOTOR_MAKSIMUM if jenis == "motor" else TARIF_MOBIL_MAKSIMUM
    tarif_awal = TARIF_MOTOR_PERTAMA if jenis == "motor" else TARIF_MOBIL_PERTAMA
    tarif_next = TARIF_MOTOR_BERIKUTNYA if jenis == "motor" else TARIF_MOBIL_BERIKUTNYA

    if not menginap:
        if durasi <= BATAS_GRATIS_MENIT:
            tarif_dasar = 0
        else:
            tarif_dasar = tarif_awal + (jam_ditagih - 1) * tarif_next
            if tarif_dasar > tarif_maks:
                tarif_dasar = tarif_maks
    else:
        # Menginap: Hari masuk kena tarif harian maksimal + tarif berjalan hari keluar
        jam_hari_keluar = (waktu_keluar + MENIT_PER_JAM - 1) // MENIT_PER_JAM
        if jam_hari_keluar == 0:
            tarif_hari_keluar = 0
        else:
            tarif_hari_keluar = tarif_awal + (jam_hari_keluar - 1) * tarif_next
            if tarif_hari_keluar > tarif_maks:
                tarif_hari_keluar = tarif_maks
        tarif_dasar = tarif_maks + tarif_hari_keluar

    if kartu == "ya" and tiket_hilang != "ya" and tarif_dasar > 0:
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
    print("Status      :", "Menginap (Keluar Hari ke-" + str(hari_keluar) + ")" if menginap else "Reguler (Hari ke-" + str(hari_keluar) + ")")
    print("Jenis       :", jenis)
    print("Durasi      :", durasi // MENIT_PER_JAM, "jam", durasi % MENIT_PER_JAM, "menit")
    print("Jam ditagih :", jam_ditagih)
    print("Tarif dasar : Rp", tarif_dasar)
    print("Diskon      : Rp", diskon)
    print("Denda       : Rp", denda)
    print("TOTAL       : Rp", total)
    print()

    # Perbarui rekap berdasarkan hari keluar
    if hari_keluar not in rekap_harian:
        rekap_harian[hari_keluar] = {
            "jumlah_kendaraan": 0,
            "jumlah_motor": 0,
            "jumlah_mobil": 0,
            "jumlah_gratis": 0,
            "jumlah_diskon": 0,
            "jumlah_denda": 0,
            "total_pendapatan": 0,
            "durasi_terlama": 0,
            "plat_terlama": "",
            "bayar_tertinggi": 0,
            "plat_bayar_tertinggi": ""
        }

    rekap = rekap_harian[hari_keluar]
    rekap["jumlah_kendaraan"] += 1
    if jenis == "motor":
        rekap["jumlah_motor"] += 1
    else:
        rekap["jumlah_mobil"] += 1

    if tarif_dasar == 0:
        rekap["jumlah_gratis"] += 1
    if diskon > 0:
        rekap["jumlah_diskon"] += 1
    if denda > 0:
        rekap["jumlah_denda"] += 1

    rekap["total_pendapatan"] += total

    if durasi > rekap["durasi_terlama"]:
        rekap["durasi_terlama"] = durasi
        rekap["plat_terlama"] = plat

    if total > rekap["bayar_tertinggi"]:
        rekap["bayar_tertinggi"] = total
        rekap["plat_bayar_tertinggi"] = plat

    # Baca plat berikutnya
    plat = input("Plat nomor (ketik SELESAI untuk berhenti): ")

# TAHAP 5: Rekap Akhir per Hari
print()
print("===== REKAP KESELURUHAN PER HARI KELUAR =====")
if not rekap_harian:
    print("Belum ada kendaraan yang tercatat.")
else:
    for hari in sorted(rekap_harian.keys()):
        data = rekap_harian[hari]
        rata_rata = data["total_pendapatan"] // data["jumlah_kendaraan"]
        print(f"\n--- REKAP HARI KE-{hari} ---")
        print("Jumlah kendaraan   :", data["jumlah_kendaraan"])
        print("  Motor            :", data["jumlah_motor"])
        print("  Mobil            :", data["jumlah_mobil"])
        print("Parkir gratis      :", data["jumlah_gratis"])
        print("Mendapat diskon    :", data["jumlah_diskon"])
        print("Kena denda tiket   :", data["jumlah_denda"])
        print("Total pendapatan   : Rp", data["total_pendapatan"])
        print("Rata-rata/kendaraan: Rp", rata_rata)
        print("Parkir terlama     :", data["plat_terlama"], "(",
              data["durasi_terlama"] // MENIT_PER_JAM, "jam",
              data["durasi_terlama"] % MENIT_PER_JAM, "menit )")
        print("Bayar tertinggi    :", data["plat_bayar_tertinggi"], "( Rp", data["bayar_tertinggi"], ")")
        print("Grafik jumlah kendaraan:")
        print("Motor |", "#" * data["jumlah_motor"])
        print("Mobil |", "#" * data["jumlah_mobil"])
