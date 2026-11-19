TARIF_PERTAMA_MOTOR = 2000
TARIF_LANJUT_MOTOR = 1000
TARIF_MAKS_MOTOR = 8000
TARIF_PERTAMA_MOBIL = 4000
TARIF_LANJUT_MOBIL = 2000
TARIF_MAKS_MOBIL = 16000

MAKS_MENIT_GRATIS = 15
DISKON_PERSEN = 20
DENDA_HILANG = 10000
KODE_BERHENTI = "SELESAI"
MENIT_SEJAM = 60

print("===== PARKIRKU KAMPUS SURABAYA =====")
print("Tabel Tarif:")
print("Jam | Motor | Mobil")
tabel_motor = TARIF_PERTAMA_MOTOR
tabel_mobil = TARIF_PERTAMA_MOBIL
for jam in range(1, 9):
    if jam > 1:
        tabel_motor = tabel_motor + TARIF_LANJUT_MOTOR
        tabel_mobil = tabel_mobil + TARIF_LANJUT_MOBIL
    if tabel_motor > TARIF_MAKS_MOTOR:
        tabel_motor = TARIF_MAKS_MOTOR
    if tabel_mobil > TARIF_MAKS_MOBIL:
        tabel_mobil = TARIF_MAKS_MOBIL
    print(jam, "  | Rp", tabel_motor, "| Rp", tabel_mobil)
print()

total_kendaraan = 0
total_motor = 0
total_mobil = 0
total_gratis = 0
total_diskon = 0
total_denda = 0
uang_masuk = 0
menit_terlama = 0
plat_terlama = ""
bayar_maks = 0
plat_bayar_maks = ""

selesai = False
while not selesai:
    plat = input("Plat nomor (ketik SELESAI untuk berhenti): ")

    if plat == KODE_BERHENTI:
        selesai = True
    else:
        jenis = ""
        while not (jenis == "motor" or jenis == "mobil"):
            jenis = input("Jenis kendaraan (motor/mobil): ")
            if not (jenis == "motor" or jenis == "mobil"):
                print("Jenis harus motor atau mobil.")

        if jenis == "motor":
            tarif_pertama = TARIF_PERTAMA_MOTOR
            tarif_lanjut = TARIF_LANJUT_MOTOR
            tarif_maks = TARIF_MAKS_MOTOR
        else:
            tarif_pertama = TARIF_PERTAMA_MOBIL
            tarif_lanjut = TARIF_LANJUT_MOBIL
            tarif_maks = TARIF_MAKS_MOBIL

        jam_masuk = -1
        while jam_masuk < 0 or jam_masuk > 23:
            jam_masuk = int(input("Jam masuk (0-23): "))
            if jam_masuk < 0 or jam_masuk > 23:
                print("Waktu tidak valid.")
        menit_masuk = -1
        while menit_masuk < 0 or menit_masuk > 59:
            menit_masuk = int(input("Menit masuk (0-59): "))
            if menit_masuk < 0 or menit_masuk > 59:
                print("Waktu tidak valid.")
        masuk = jam_masuk * MENIT_SEJAM + menit_masuk

        keluar = -1
        while keluar < masuk:
            jam_keluar = -1
            while jam_keluar < 0 or jam_keluar > 23:
                jam_keluar = int(input("Jam keluar (0-23): "))
                if jam_keluar < 0 or jam_keluar > 23:
                    print("Waktu tidak valid.")
            menit_keluar = -1
            while menit_keluar < 0 or menit_keluar > 59:
                menit_keluar = int(input("Menit keluar (0-59): "))
                if menit_keluar < 0 or menit_keluar > 59:
                    print("Waktu tidak valid.")
            keluar = jam_keluar * MENIT_SEJAM + menit_keluar
            if keluar < masuk:
                print("Waktu keluar tidak boleh sebelum waktu masuk.")

        kartu = ""
        while kartu != "ya" and kartu != "tidak":
            kartu = input("Punya kartu civitas? (ya/tidak): ")
            if kartu != "ya" and kartu != "tidak":
                print("Jawaban harus ya atau tidak.")

        hilang = ""
        while hilang != "ya" and hilang != "tidak":
            hilang = input("Tiket hilang? (ya/tidak): ")
            if hilang != "ya" and hilang != "tidak":
                print("Jawaban harus ya atau tidak.")

        durasi = keluar - masuk
        jam_ditagih = 0
        sisa = durasi
        while sisa > 0:
            jam_ditagih = jam_ditagih + 1
            sisa = sisa - MENIT_SEJAM

        tarif_dasar = 0
        if durasi > MAKS_MENIT_GRATIS:
            tarif_dasar = tarif_pertama
            for j in range(2, jam_ditagih + 1):
                tarif_dasar = tarif_dasar + tarif_lanjut
            if tarif_dasar > tarif_maks:
                tarif_dasar = tarif_maks

        diskon = 0
        if kartu == "ya" and hilang == "tidak" and tarif_dasar > 0:
            diskon = tarif_dasar * DISKON_PERSEN // 100

        denda = 0
        if hilang == "ya":
            denda = DENDA_HILANG

        total = tarif_dasar - diskon + denda

        print()
        print("--- STRUK", plat, "---")
        print("Jenis       :", jenis)
        print("Durasi      :", durasi // MENIT_SEJAM, "jam", durasi % MENIT_SEJAM, "menit")
        print("Jam ditagih :", jam_ditagih)
        print("Tarif dasar : Rp", tarif_dasar)
        print("Diskon      : Rp", diskon)
        print("Denda       : Rp", denda)
        print("TOTAL       : Rp", total)
        print()

        total_kendaraan = total_kendaraan + 1
        if jenis == "motor":
            total_motor = total_motor + 1
        else:
            total_mobil = total_mobil + 1
        if tarif_dasar == 0:
            total_gratis = total_gratis + 1
        if diskon > 0:
            total_diskon = total_diskon + 1
        if denda > 0:
            total_denda = total_denda + 1
        uang_masuk = uang_masuk + total
        if durasi > menit_terlama:
            menit_terlama = durasi
            plat_terlama = plat
        if total > bayar_maks:
            bayar_maks = total
            plat_bayar_maks = plat

print()
print("===== REKAP PARKIR HARI INI =====")
if total_kendaraan == 0:
    print("Belum ada kendaraan yang tercatat.")
else:
    print("Jumlah kendaraan   :", total_kendaraan)
    print("  Motor            :", total_motor)
    print("  Mobil            :", total_mobil)
    print("Parkir gratis      :", total_gratis)
    print("Mendapat diskon    :", total_diskon)
    print("Kena denda tiket   :", total_denda)
    print("Total pendapatan   : Rp", uang_masuk)
    print("Rata-rata/kendaraan: Rp", uang_masuk // total_kendaraan)
    print("Parkir terlama     :", plat_terlama, "(", menit_terlama // MENIT_SEJAM,
          "jam", menit_terlama % MENIT_SEJAM, "menit )")
    print("Bayar tertinggi    :", plat_bayar_maks, "( Rp", bayar_maks, ")")
    print("Grafik jumlah kendaraan:")
    garis_motor = ""
    for i in range(total_motor):
        garis_motor = garis_motor + "#"
    garis_mobil = ""
    for i in range(total_mobil):
        garis_mobil = garis_mobil + "#"
    print("Motor |", garis_motor)
    print("Mobil |", garis_mobil)