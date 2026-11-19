# Praktikum Algoritma dan Pemrograman (Python)

Repositori ini berisi kumpulan program latihan, studi kasus praktikum, serta mini project mata kuliah **Algoritma dan Pemrograman (S1 Sistem Informasi)** menggunakan bahasa pemrograman **Python 3**, disusun secara terstruktur berdasarkan modul praktikum mingguan (*weekly modules*).

---

## 📚 Daftar Isi

- [Identitas](#-identitas)
- [Week 1: Variabel, Tipe Data, dan Percabangan (if-else)](#-week-1-variabel-tipe-data-dan-percabangan-if-else)
- [Week 2: Percabangan Bertingkat dan Perulangan Dasar](#-week-2-percabangan-bertingkat-dan-perulangan-dasar)
- [Week 3: Pola Perulangan (Penelusuran, Kondisi Batas, dan Sentinel)](#-week-3-pola-perulangan-penelusuran-kondisi-batas-dan-sentinel)
- [Week 4: Pola Pengolahan Data Lanjut (Penyaringan, Nilai Ekstrem, dan Rekapitulasi)](#-week-4-pola-pengolahan-data-lanjut-penyaringan-nilai-ekstrem-dan-rekapitulasi)
- [Week 5: Fungsi, Parameter, dan Nilai Kembalian](#-week-5-fungsi-parameter-dan-nilai-kembalian)
- [Mini Project: Sistem Manajemen ParkirKu](#-mini-project-sistem-manajemen-parkirku)
- [Struktur Direktori](#-struktur-direktori)
- [Cara Menjalankan Kode](#-cara-menjalankan-kode)

---

## 👤 Identitas

```py
Nama          : Dendra De Tama
NIM           : 108052600034
Program Studi : S1 Sistem Informasi
Institusi     : Telkom University Surabaya
Mata Kuliah   : Algoritma dan Pemrograman (BBK1AAB4)
Dosen Pengampu: Adzanil Rachmadhi Putra
```

---

## 📌 Week 1: Variabel, Tipe Data, dan Percabangan (if-else)

Fokus pada pengenalan sintaks dasar Python, aturan penamaan variabel, tipe data primitif, input/output interaktif, serta evaluasi keputusan bersyarat (`if`, `elif`, `else`).

### Materi Utama:
1. **Variabel & Aturan Penamaan**: Penggunaan gaya *snake_case*, sifat *case-sensitive*, dan alokasi memori dinamis.
2. **Tipe Data Dasar**: Karakteristik `str`, `int`, `float`, dan `bool`, serta verifikasi tipe via `type()`.
3. **Input Pengguna & Konversi Tipe**: Fungsi `input()` dan *type casting* eksplisit (`int()`, `float()`).
4. **Struktur Percabangan**: Percabangan biner dan berantai untuk klasifikasi data numerik.

### Rincian File:
- `latihan1.py` : Deklarasi variabel multi-tipe dan inspeksi kelas tipe data menggunakan `type()`.
- `latihan2.py` : Pembacaan masukan nama dan usia serta casting eksplisit untuk kalkulasi aritmatika.
- `latihan3.py` : Percabangan biner (`if-else`) dan operator modulo `%` untuk deteksi bilangan ganjil/genap.
- `latihan4.py` : Percabangan berantai (`if-elif-else`) untuk penentuan kategori nilai ujian (A/B/C/D).
- `studi_kasus.py` : Program Cek Kelulusan Mahasiswa (ambang batas $\ge 60$) beserta tantangan penentuan grade huruf.
- `Readme.md` : Laporan lengkap praktikum Week 1.

---

## 📌 Week 2: Percabangan Bertingkat dan Perulangan Dasar

Mendalami pengambilan keputusan multi-tahap (*nested if*) dan pengenalan konsep perulangan terkontrol (*definite loop*) serta perulangan bersyarat (*indefinite loop*).

### Materi Utama:
1. **Percabangan Bertingkat (*Nested If*)**: Struktur `if` bersarang untuk keputusan yang memiliki prasyarat bertingkat.
2. **Perulangan `for` & `range()`**: Enumerasi terhitung dengan argumen rentang dan langkah (*step*).
3. **Perulangan `while`**: Eksekusi blok instruksi selama kondisi bernilai `True`.
4. **Pengendali Alur Iterasi**:
   - `break` : Terminasi paksa seluruh proses perulangan.
   - `continue` : Memotong iterasi saat ini dan langsung melompat ke iterasi berikutnya.

### Rincian File:
- `latihan1.py` : Validasi usia menonton film 17+ dan pengecekan kepemilikan kartu pelajar untuk harga tiket.
- `latihan2.py` : Perulangan `for` dan fungsi `range(1, 6)` untuk mencetak deret 1–5 dan tabel perkalian 3.
- `latihan3.py` : Perulangan `while` akumulatif berbasis *sentinel value* (berhenti ketika input angka bernilai `0`).
- `latihan4.py` : Simulasi instruksi `break` (berhenti di angka 8) dan `continue` (menyaring bilangan genap).
- `studi_kasus.py` : Program Rekap Nilai Kuis Kelas (*input guard* 0–100 via `while`, klasifikasi 4 kategori kelulusan, rata-rata, nilai tertinggi, dan nilai terendah).
- `Readme.md` : Laporan lengkap praktikum Week 2.

---

## 📌 Week 3: Pola Perulangan (Penelusuran, Kondisi Batas, dan Sentinel)

Fokus pada verifikasi keandalan logika perulangan, analisis jaminan berhenti (*termination guarantee*), pencegahan galat batas (*off-by-one*), dan masukan berpenanda (*sentinel*).

### Materi Utama:
1. **Tabel Penelusuran (*Trace Table*)**: Penelusuran variabel langkah demi langkah untuk memvalidasi algoritma sebelum dieksekusi.
2. **Jaminan Berhenti & Kondisi Batas**: Memastikan terminasi loop dan mencegah galat inklusivitas (`<` vs `<=`).
3. **Masukan Berpenanda (*Sentinel Loop*)**: Pola pembacaan data ganda (*read-twice*) saat kuantitas data dinamis.
4. **Pola Akumulator & Pencacah**: Akumulasi nilai (`total = total + x`) dan pencacahan frekuensi (`banyak = banyak + 1`).

### Rincian File:
- `latihan1.py` : Tabel penelusuran `while` loop penjumlahan kelipatan dua ($n=1..5$, total = 30).
- `latihan2.py` : Analisis dan koreksi kesalahan kondisi batas penjumlahan deret 1 s.d. $n$ (`i <= n`).
- `latihan3.py` : Masukan waktu proses berpenanda sentinel `-1` dengan proteksi pembagian nol (*zero-division guard*).
- `latihan4.py` : Rekapitulasi target produksi 10 hari lini pabrik memadukan pola akumulator dan pencacah harian.
- `Readme.md` : Laporan lengkap praktikum Week 3.

---

## 📌 Week 4: Pola Pengolahan Data Lanjut (Penyaringan, Nilai Ekstrem, dan Rekapitulasi)

Melanjutkan pengolahan data terpadu: penyaringan data bersyarat, pelacakan nilai ekstrem (maksimum/minimum) secara aman, serta dekomposisi masalah komputasi (*problem grouping*).

### Materi Utama:
1. **Pola Penyaringan (*Filtering*)**: Mengintegrasikan kondisi `if` di dalam loop agar komputasi hanya memproses data yang lolos kriteria.
2. **Nilai Ekstrem & Jebakan Inisialisasi**: Menghindari bias inisialisasi awal `0` dengan menerapkan sentinel `None` atau data pertama pada himpunan data bernilai negatif.
3. **Pelacakan Indeks Posisi Ekstrem**: Menyimpan urutan atau periode waktu saat nilai ekstrem terjadi dengan penanganan nilai kembar terawal (*earliest tie-breaker*).
4. **Dekomposisi Masalah (*Problem Grouping*)**: Memetakan sub-masalah kompleks ke pola standar algoritma.

### Rincian File:
- `latihan1.py` : Pola penyaringan produksi yang mencapai target ($\ge 50$ unit) beserta kalkulasi rata-rata tersaring.
- `latihan2.py` : Pencarian laba bulanan tertinggi pada data negatif dengan inisialisasi `None` dan pencatatan bulan kejadian.
- `latihan3.py` : Pengelompokan masalah analisis 8 pencatatan suhu mesin (suhu tertinggi, pencacah $> 80^\circ$, dan rata-rata suhu yang lolos).
- `studi_kasus.py` : Program Rekap Produksi Lini Perakitan (sentinel `-1`, target 100 unit, pemutus seri ekstrem terawal, dan rata-rata produksi khusus hari target).
- `Readme.md` : Laporan lengkap praktikum Week 4.

---

## 📌 Week 5: Fungsi, Parameter, dan Nilai Kembalian

Fokus pada modularisasi kode menggunakan fungsi di Python 3 untuk meningkatkan keterbacaan, efisiensi, pengujian independen, dan pemeliharaan kode (*maintainability*).

### Materi Utama:
1. **Anatomi Fungsi (`def`)**: Pembuatan fungsi, parameter formal, argumen aktual, dan *single responsibility*.
2. **Nilai Kembalian (`return`) vs `print`**: Mengembalikan data hasil perhitungan ke alur pemanggil versus sekadar mencetak teks ke layar.
3. **Fungsi Predikat Boolean**: Fungsi penghasil nilai `True` atau `False` yang dapat langsung menjadi ekspresi percabangan `if`.
4. **Pustaka Standar Python**: Pemanfaatan modul bawaan `math` (`sqrt`, `ceil`) dan `random` (`randint`).
5. **Konsep Rekursi Dasar**: Mekanisme fungsi memanggil dirinya sendiri yang dikontrol oleh *base case* untuk mencegah `RecursionError`.

### Rincian File:
- `latihan1.py` : Prosedur cetak tanpa return (`cetak_garis` dan `kartu_nama`) yang memanggil fungsi lain.
- `latihan2.py` : Fungsi return konversi suhu (`celsius_ke_fahrenheit`) dan perhitungan geometris (`luas_persegi_panjang`).
- `latihan3.py` : Early return pada grade huruf (`nilai_huruf`) dan fungsi predikat kelulusan boolean (`lulus`).
- `latihan4.py` : Implementasi modul `math` (jarak Euclidean) dan simulasi dadu acak dengan modul `random`.
- `latihan5.py` : Algoritma rekursif perhitungan faktorial matematika dan simulasi hitung mundur.
- `studi_kasus.py` : Kalkulator Nilai Akhir Mahasiswa modular (`nilai_valid`, `baca_nilai`, `nilai_akhir`, `nilai_huruf`, dan fungsi `rata_rata` terlindung pembagian nol).
- `Readme.md` : Laporan lengkap praktikum Week 5.

---

## 🅿️ Mini Project: Sistem Manajemen ParkirKu

Proyek berbasis konsol (`MiniProject/`) yang mensimulasikan sistem pencatatan transaksi keluar kendaraan parkir harian secara otomatis dan defensif.

### Fitur Utama:
- Pengelompokan tarif motor dan mobil (tarif jam pertama, jam berikutnya, tarif maksimal harian, gratis 15 menit awal, diskon civitas 20%, dan denda tiket hilang).
- *Defensive input validation*: Validasi jenis kendaraan, validasi jam (0–23) dan menit (0–59), serta kronologi waktu keluar terhadap waktu masuk.
- Pencatatan transaksi berpenanda pelat nomor `SELESAI`.
- Rekapitulasi akhir: Statistik pendapatan total, rata-rata, durasi parkir terlama, biaya tertinggi, serta visualisasi diagram batang karakter `#`.
- Berkas: `parkir.py`, `parkir2.py`, `help.py`, dan `Readme.md`.

---

## 📂 Struktur Direktori

```text
Praktikum-Alpro/
├── Week-1/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   ├── studi_kasus.py
│   └── Readme.md
├── Week-2/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   ├── studi_kasus.py
│   └── Readme.md
├── Week-3/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   └── Readme.md
├── Week-4/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── studi_kasus.py
│   └── Readme.md
├── Week-5/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   ├── latihan5.py
│   ├── studi_kasus.py
│   └── Readme.md
├── MiniProject/
│   ├── help.py
│   ├── parkir.py
│   ├── parkir2.py
│   └── Readme.md
└── Readme.md
```

---

## 🚀 Cara Menjalankan Kode

1. Buka terminal atau Command Prompt / PowerShell.
2. Masuk ke direktori folder praktikum yang ingin dijalankan, misalnya:
   ```bash
   cd Week-5
   ```
3. Jalankan berkas program menggunakan interpreter Python 3:
   ```bash
   python studi_kasus.py
   # atau berkas latihan lainnya:
   python latihan1.py
   ```
4. Untuk menjalankan Mini Project ParkirKu:
   ```bash
   cd MiniProject
   python parkir.py
   ```
