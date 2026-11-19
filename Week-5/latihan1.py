def cetak_garis(panjang):
    print("=" * panjang)


def kartu_nama(nama, prodi):
    cetak_garis(30)
    print("Nama  :", nama)
    print("Prodi :", prodi)
    cetak_garis(30)


kartu_nama("Rani", "Sistem Informasi")
kartu_nama("Dimas", "Sistem Informasi")
