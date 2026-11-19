# Laporan Tugas Individu #1 — ParkirKu

## 1. Identitas Diri

| | |
| :--- | :--- |
| **Nama** | Dendra De Tama |
| **NIM** | 108052600034 |
| **Kelas** | SS1SI-50-REG-01 |
| **Dosen** | Adzanil Rachmadhi Putra |
| **Mata Kuliah** | Algoritma dan Pemrograman |

---

## 2. Deskripsi Program

ParkirKu Kampus Surabaya adalah program berbasis teks (console) dalam satu berkas `parkir.py` yang mencatat kendaraan keluar dari area parkir selama satu hari, menghitung biaya tiap kendaraan, mencetak struk, lalu menampilkan rekap saat petugas mengetik `SELESAI`. Program mendukung dua jenis kendaraan (motor dan mobil) dengan tarif jam pertama, tarif jam berikutnya, batas maksimum per hari, gratis 15 menit pertama, diskon civitas 20%, dan denda tiket hilang Rp 10000. Seluruh angka aturan disimpan sebagai konstanta bernama di bagian atas program, dan tabel tarif 1 sampai 8 jam dicetak di awal dengan `for` dan `range()`.

Program tidak mempercayai masukan: jenis kendaraan, rentang jam (0-23) dan menit (0-59), urutan waktu keluar terhadap waktu masuk, serta jawaban kartu dan tiket divalidasi dengan `while` sampai benar. Perulangan transaksi memakai plat `SELESAI` sebagai penanda tanpa `while True`, `break`, maupun `continue`. Rekap akhir berisi jumlah kendaraan per jenis, jumlah gratis, berdiskon, dan kena denda, total pendapatan, rata-rata (pembagian bulat), parkir terlama, bayar tertinggi, dan grafik batang `#`. Kasus data kosong ditangani sehingga tidak terjadi pembagian nol.

---

## 3. Dekomposisi Masalah

Nomor baris mengacu pada `parkir.py` yang dikumpulkan. Baris bertanda *(tersirat)* adalah sub-masalah yang tidak ditulis eksplisit di soal.

| Sub-Masalah | Plan Pemrograman | Letak (Tahap / Baris) | Keterangan |
| :--- | :--- | :--- | :--- |
| Menyimpan aturan tarif | Konstanta bernama | Tahap 1, baris 3-22 | Semua angka aturan dan kata `SELESAI` ada di atas program |
| Mencetak tabel tarif 1-8 jam | Perulangan terhitung (`for` + `range`) | Tahap 1, baris 29-38 | Rumus sama dengan Tahap 3, sudah dibatasi maksimum |
| Nilai awal variabel rekap | Inisialisasi pencacah, akumulator, ekstrem | Tahap 1, baris 40-50 | Pencacah dan akumulator mulai dari 0 |
| Nilai awal variabel ekstrem *(tersirat)* | Nilai awal di luar rentang valid | Baris 24, 47, 49 | `NILAI_AWAL_EKSTREM = -1`, alasan di bagian 4 |
| Berhenti saat petugas mengetik SELESAI | Masukan berpenanda (*sentinel*) | Tahap 4, baris 54, 56, 163 | Baca plat sebelum `while` dan di akhir blok |
| Validasi jenis kendaraan | Penjaga masukan (*input guard*) | Tahap 2, baris 60-63 | Hanya `motor` atau `mobil` |
| Validasi jam dan menit masuk | Penjaga rentang + variabel penanda `sah` | Tahap 2, baris 66-73 | Jam 0-23 dan menit 0-59, diulang bersama |
| Konversi waktu ke menit *(tersirat)* | Transformasi `jam * 60 + menit` | Baris 75 dan 82 | Memudahkan selisih dan perbandingan waktu |
| Validasi waktu keluar | Penjaga rentang + penjaga relasi | Tahap 2, baris 78-89 | Rentang valid dan `waktu_keluar >= waktu_masuk` |
| Validasi kartu dan tiket | Penjaga masukan | Tahap 2, baris 91-99 | Hanya `ya` atau `tidak` |
| Menghitung durasi | Aritmatika | Tahap 3, baris 103 | `waktu_keluar - waktu_masuk` dalam menit |
| Pembulatan jam ke atas *(tersirat)* | Pembagian bulat pembulatan atas (*ceiling*) | Tahap 3, baris 104 | `(durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM` |
| Tarif dasar, batas gratis, batas maksimum | Percabangan `if-elif-else` + pembatasan nilai (*clamping*) | Tahap 3, baris 106-115 | Durasi <= 15 menit gratis, lalu dipotong ke maksimum |
| Diskon civitas | Penyaring bersyarat (`and`) | Tahap 3, baris 117-121 | Kartu `ya` dan tiket tidak hilang dan tarif dasar > 0 |
| Denda tiket hilang | Percabangan | Tahap 3, baris 123-127 | Tetap berlaku walau durasi gratis |
| Total dan struk | Aritmatika + cetak | Tahap 3, baris 129-141 | `total = tarif_dasar - diskon + denda` |
| Pencacah jumlah, motor, mobil | Pencacah | Tahap 4, baris 143-148 | |
| Pencacah gratis, diskon, denda | Penyaringan + pencacah | Tahap 4, baris 149-153 | Hanya yang memenuhi syarat dihitung |
| Total pendapatan | Akumulator | Tahap 4, baris 154 | |
| Parkir terlama dan bayar tertinggi | Nilai ekstrem | Tahap 4, baris 155-160 | Memakai `>` agar bila seri yang lebih dulu tetap |
| Data kosong *(tersirat)* | Penjaga pembagian nol | Tahap 5, baris 169-171 | Cetak pesan, tidak hitung rata-rata dan ekstrem |
| Rata-rata per kendaraan | Akumulator ÷ pencacah | Tahap 5, baris 172 | Pembagian bulat `//` |
| Grafik batang teks | Akumulator string (`for` + `range`) | Tahap 5, baris 185-192 | Satu `#` untuk satu kendaraan |

---

## 4. Flowchart dan Pseudocode Tahap 3 (Hitung Biaya)

### Flowchart

![Flowchart Tahap 3](./Tahap3Flowchart.png)

### Pseudocode

```text
ALGORITMA HitungBiayaDanStruk
MASUKAN : plat, jenis, waktu_masuk, waktu_keluar, kartu, tiket_hilang
KELUARAN: durasi, jam_ditagih, tarif_dasar, diskon, denda, total

DEKLARASI:
    durasi, jam_ditagih, tarif_dasar, diskon, denda, total : INTEGER

PROSES:
    durasi <- waktu_keluar - waktu_masuk
    jam_ditagih <- (durasi + MENIT_PER_JAM - 1) DIV MENIT_PER_JAM

    JIKA durasi <= BATAS_GRATIS_MENIT MAKA
        tarif_dasar <- 0
    SELAIN ITU JIKA jenis = "motor" MAKA
        tarif_dasar <- TARIF_MOTOR_PERTAMA + (jam_ditagih - 1) * TARIF_MOTOR_BERIKUTNYA
        JIKA tarif_dasar > TARIF_MOTOR_MAKSIMUM MAKA
            tarif_dasar <- TARIF_MOTOR_MAKSIMUM
        AKHIR JIKA
    SELAIN ITU
        tarif_dasar <- TARIF_MOBIL_PERTAMA + (jam_ditagih - 1) * TARIF_MOBIL_BERIKUTNYA
        JIKA tarif_dasar > TARIF_MOBIL_MAKSIMUM MAKA
            tarif_dasar <- TARIF_MOBIL_MAKSIMUM
        AKHIR JIKA
    AKHIR JIKA

    JIKA kartu = "ya" DAN tiket_hilang = "tidak" DAN tarif_dasar > 0 MAKA
        diskon <- (tarif_dasar * PERSEN_DISKON) DIV PERSEN_PENUH
    SELAIN ITU
        diskon <- 0
    AKHIR JIKA

    JIKA tiket_hilang = "ya" MAKA
        denda <- DENDA_TIKET_HILANG
    SELAIN ITU
        denda <- 0
    AKHIR JIKA

    total <- tarif_dasar - diskon + denda

    TAMPILKAN Struk(plat, jenis, durasi, jam_ditagih, tarif_dasar, diskon, denda, total)
SELESAI
```

---

## 5. Tabel Penelusuran

Data penelusuran (bagian 5.1 soal), dihitung dengan tangan sebelum program dijalankan:

| Plat | Jenis | Masuk | Keluar | Kartu | Tiket hilang | Urutan |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| A 1111 AA | motor | 13:00 | 13:40 | tidak | tidak | Pertama |
| B 2222 BB | mobil | 06:50 | 09:10 | ya | tidak | Kedua |
| C 3333 CC | motor | 15:00 | 15:15 | tidak | tidak | Ketiga |

| Kendaraan ke- | durasi | jam_tagih | tarif_dasar | diskon | total | jumlah | total_pendapatan | durasi_terlama |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Awal** | - | - | - | - | - | 0 | 0 | -1 |
| **1** | 40 | 1 | 2000 | 0 | 2000 | 1 | 2000 | 40 |
| **2** | 140 | 3 | 8000 | 1600 | 6400 | 2 | 8400 | 140 |
| **3** | 15 | 1 | 0 | 0 | 0 | 3 | 8400 | 140 |

### Perbandingan dengan hasil program

Ketiga kendaraan dimasukkan ke `parkir.py`. Hasil program **sama dengan hasil hitung tangan**: durasi 40, 140, dan 15 menit; jam ditagih 1, 3, dan 1; total Rp 2000, Rp 6400, dan Rp 0; jumlah kendaraan 3; total pendapatan Rp 8400; parkir terlama B 2222 BB (2 jam 20 menit = 140 menit); bayar tertinggi B 2222 BB (Rp 6400). Satu catatan: struk program menampilkan durasi dalam format jam dan menit (2 jam 20 menit), yaitu nilai 140 menit yang sama dengan tabel.


### Uraian perhitungan
1. **A 1111 AA (motor)**: waktu_masuk = 13 × 60 + 0 = 780; waktu_keluar = 13 × 60 + 40 = 820; durasi = 40 menit; jam_tagih = (40 + 59) // 60 = 1; tarif_dasar = 2000 + 0 × 1000 = 2000; diskon = 0 (tidak punya kartu); total = 2000. Rekap: jumlah = 1, total_pendapatan = 2000, durasi_terlama = 40.
2. **B 2222 BB (mobil)**: waktu_masuk = 6 × 60 + 50 = 410; waktu_keluar = 9 × 60 + 10 = 550; durasi = 140 menit; jam_tagih = (140 + 59) // 60 = 3; tarif_dasar = 4000 + 2 × 2000 = 8000; diskon = 8000 × 20 // 100 = 1600; total = 6400. Rekap: jumlah = 2, total_pendapatan = 8400, durasi_terlama = 140.
3. **C 3333 CC (motor)**: waktu_masuk = 900; waktu_keluar = 915; durasi = 15 menit; jam_tagih = (15 + 59) // 60 = 1; durasi <= 15 sehingga tarif_dasar = 0; diskon = 0; total = 0. Rekap: jumlah = 3, total_pendapatan = 8400, durasi_terlama tetap 140 karena 15 tidak lebih besar dari 140.

---

## 6. Tabel Kasus Uji

Seluruh kasus dijalankan pada `parkir.py` (Python 3.12) dan kolom hasil program diisi dari output aktual.

| No | Kategori | Masukan | Hasil yang Diharapkan | Hasil Program | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Normal | L 1234 AB, motor, 08:00-11:20, kartu ya, tiket hilang tidak | Jam ditagih 4, tarif Rp 5000, diskon Rp 1000, total Rp 4000 | Total Rp 4000 | PASS |
| 2 | Normal | N 7788 IJ, mobil, 12:00-14:10, kartu tidak, tiket hilang tidak | Jam ditagih 3, tarif Rp 8000, diskon Rp 0, total Rp 8000 | Total Rp 8000 | PASS |
| 3 | Normal | L 3456 GH, motor, 10:00-10:16, kartu ya, tiket hilang ya | Tarif Rp 2000, diskon Rp 0 (batal), denda Rp 10000, total Rp 12000 | Total Rp 12000, diskon Rp 0 | PASS |
| 4 | Batas | W 5678 CD, mobil, 09:00-09:15 (tepat 15 menit) | Gratis: tarif Rp 0, total Rp 0 | Total Rp 0 | PASS |
| 5 | Batas | Motor, 10:00-10:16 (16 menit), tanpa kartu dan tiket aman | Jam ditagih 1, tarif Rp 2000 | Tarif Rp 2000, total Rp 2000 | PASS |
| 6 | Batas | S 9012 EF, motor, 07:30-19:45, kartu ya | Jam ditagih 13, tarif dipotong ke Rp 8000, diskon Rp 1600, total Rp 6400 | Jam ditagih 13, total Rp 6400 | PASS |
| 7 | Batas | Motor, 08:00-15:00 (7 jam, tepat di tarif maksimum) | Tarif Rp 8000 | Tarif Rp 8000, total Rp 8000 | PASS |
| 8 | Batas | Motor, masuk 10:00 keluar 10:00 (durasi 0 menit) | Total Rp 0; rekap tetap mencatat plat terlama dan bayar tertinggi | Total Rp 0; rekap: terlama X 1 A (0 jam 0 menit), bayar tertinggi X 1 A (Rp 0) | PASS |
| 9 | Batas | Mobil, 00:00-23:59 (jam 23 menit 59) | Jam ditagih 24, tarif dipotong ke Rp 16000 | Jam ditagih 24, total Rp 16000 | PASS |
| 10 | Batas | Mobil, 09:00-09:10 (gratis), kartu ya, tiket hilang ya | Tarif Rp 0, diskon Rp 0, denda Rp 10000, total Rp 10000 | Denda Rp 10000, total Rp 10000 | PASS |
| 11 | Batas | Langsung ketik `SELESAI` (data kosong) | Cetak "Belum ada kendaraan yang tercatat.", tanpa galat | Pesan tercetak, tanpa galat | PASS |
| 12 | Tidak valid | Jenis `truk`, lalu `mobil` | Pesan "Jenis harus motor atau mobil." lalu tanya ulang | Pesan tercetak, input diulang, `mobil` diterima | PASS |
| 13 | Tidak valid | Jam masuk 25 menit 0, lalu jam 8 menit 61, lalu jam 8 menit 0 | Pesan "Waktu tidak valid." tiap kali salah, pasangan jam-menit diulang | Pesan tercetak dua kali, 8:00 diterima | PASS |
| 14 | Tidak valid | Masuk 14:00, keluar 12:00, lalu keluar 14:30 | Pesan "Waktu keluar tidak boleh sebelum waktu masuk." lalu tanya ulang | Pesan tercetak, 14:30 diterima, total Rp 2000 | PASS |
| 15 | Tidak valid | Kartu civitas `mungkin`, lalu `ya` | Pesan "Jawaban harus ya atau tidak." lalu tanya ulang | Pesan tercetak, `ya` diterima, diskon dihitung | PASS |

---

## 7. Catatan Galat

1. **Galat sintaks (*syntax error*)**
   - *Penyebab*: tanda titik dua (`:`) tertinggal pada `while plat != PENANDA_SELESAI`.
   - *Cara menemukan*: Python menolak menjalankan berkas dan menampilkan `SyntaxError: expected ':'` beserta nomor barisnya.
   - *Perbaikan*: menambahkan titik dua di akhir baris `while`.
2. **Galat runtime (*runtime error*)**
   - *Penyebab*: `ZeroDivisionError` pada `rata_rata = total_pendapatan // jumlah_kendaraan` ketika petugas langsung mengetik `SELESAI` sehingga `jumlah_kendaraan` bernilai 0.
   - *Cara menemukan*: program berhenti mendadak saat diuji dengan data kosong (kasus uji 11).
   - *Perbaikan*: memasang percabangan `if jumlah_kendaraan == 0:` sebelum rata-rata dan nilai ekstrem dihitung.
3. **Galat logika (*logic error*)**
   - *Penyebab*: jam ditagih memakai `durasi // 60`, sehingga 65 menit dihitung 1 jam dan sisa menit tidak ditagih.
   - *Cara menemukan*: hasil struk tidak sama dengan hitungan tangan di tabel penelusuran.
   - *Perbaikan*: memakai pembulatan atas `(durasi + MENIT_PER_JAM - 1) // MENIT_PER_JAM`.
4. **Temuan tambahan (galat logika pada nilai awal ekstrem)**
   - *Penyebab*: `durasi_terlama` dan `bayar_tertinggi` semula bernilai awal 0, sehingga kendaraan berdurasi 0 menit atau semua kendaraan bertotal Rp 0 tidak pernah tercatat sebagai rekor dan plat di rekap kosong.
   - *Cara menemukan*: membandingkan kode dengan tabel penelusuran (nilai awal -1) dan menguji kasus durasi 0 menit (kasus uji 8).
   - *Perbaikan*: nilai awal diganti `NILAI_AWAL_EKSTREM = -1`.

---

## 8. Refleksi

Konsep yang paling saya pahami adalah perulangan berpenanda dan pola akumulator serta pencacah, karena alurnya sistematis untuk data yang jumlahnya tidak diketahui di awal. Bagian yang paling menantang adalah menentukan nilai awal variabel ekstrem, karena nilai 0 tampak wajar tetapi salah pada durasi 0 menit, dan validasi waktu keluar terhadap waktu masuk. Pembulatan atas dengan aritmatika bilangan bulat juga membutuhkan pemahaman tentang pembagian lantai. Keterbatasan program ini adalah belum mendukung parkir lintas hari (menginap), karena waktu keluar yang lebih kecil dari waktu masuk dianggap salah masukan akibat tidak ada masukan tanggal.

---

## 9. Pengungkapan Penggunaan AI

- **Bagian yang dibantu AI**:
  - Rumus pembulatan jam ke atas `(durasi + 59) // 60` dan struktur perulangan grafik batang `#`.
  - Penataan format tabel dokumentasi dan variasi kasus uji.
  - Peninjauan kesesuaian `parkir.py` dan README.
  - Pembuatan Pseudocode pada README.
  - Pembutan logic Grafik Jumlah Kendaraan
