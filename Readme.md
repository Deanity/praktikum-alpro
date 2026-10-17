# Praktikum Algoritma dan Pemrograman (Python)

Repositori ini berisi kumpulan kode program latihan, tugas mandiri (*task*), dan studi kasus praktikum mata kuliah **Algoritma dan Pemrograman (S1 Sistem Informasi)** menggunakan bahasa pemrograman **Python 3**.

---

## 📚 Daftar Isi

- [Week 1: Variabel, Tipe Data, dan Percabangan (if-else)](#-week-1-variabel-tipe-data-dan-percabangan-if-else)
- [Week 2: Percabangan Bertingkat dan Perulangan Dasar](#-week-2-percabangan-bertingkat-dan-perulangan-dasar)
- [Week 3: Pola Perulangan (Penelusuran, Kondisi Batas, dan Sentinel)](#-week-3-pola-perulangan-penelusuran-kondisi-batas-dan-sentinel)
- [Week 4: Pengolahan Data Lanjut (Penyaringan, Nilai Ekstrem, dan Studi Kasus)](#-week-4-pengolahan-data-lanjut-penyaringan-nilai-ekstrem-dan-studi-kasus)
- [Struktur Direktori](#-struktur-direktori)
- [Cara Menjalankan Kode](#-cara-menjalankan-kode)

---

## 📌 Week 1: Variabel, Tipe Data, dan Percabangan (if-else)

Fokus materi pada pengenalan dasar Python, deklarasi variabel, tipe data primitif, input/output interaktif, operasi aritmatika, serta struktur kontrol percabangan dasar.

### Materi Utama:
1. **Variabel & Aturan Penamaan**: Penggunaan aturan penamaan snake_case dan sifat case-sensitive.
2. **Tipe Data Dasar**: `str`, `int`, `float`, dan `bool`, serta pemeriksaan tipe data dengan `type()`.
3. **Input Pengguna & Casting**: Fungsi `input()` dan konversi eksplisit dengan `int()` / `float()`.
4. **Struktur Percabangan**: Pengambilan keputusan dengan `if`, `elif`, dan `else`.

### Rincian File:
- **Modul Praktikum:**
  - `latihan1.py` : Deklarasi variabel, variasi tipe data, dan pengecekan menggunakan `type()`.
  - `latihan2.py` : Menerima input nama dan umur pengguna serta konversi numerik untuk kalkulasi usia.
  - `latihan3.py` : Percabangan `if-else` untuk memeriksa bilangan genap atau ganjil.
  - `latihan4.py` : Percabangan `if-elif-else` untuk penentuan kategori nilai ujian (A/B/C/D).
  - `studi_kasus.py` : Program Cek Kelulusan Mahasiswa (batas kelulusan $\ge 60$) beserta tantangan kategori grade huruf.
- **Task Mandiri:**
  - `task1.py` : Input biodata mahasiswa (Nama, Umur, Fakultas, Kampus).
  - `task2.py` : Operasi aritmatika dasar (penjumlahan, pengurangan, perkalian, pembagian).
  - `task3.py` : Program validasi bilangan ganjil atau genap.
  - `task4.py` : Konversi nilai angka menjadi huruf mutu.
  - `task5.py` : Program kalkulator percabangan operator matematika sederhana.

---

## 📌 Week 2: Percabangan Bertingkat dan Perulangan Dasar

Mendalami pengambilan keputusan multi-tahap (*nested if*) dan pengenalan konsep perulangan terkontrol (*definite loop*) maupun tak tentu (*indefinite loop*).

### Materi Utama:
1. **Percabangan Bertingkat (*Nested If*)**: Struktur `if` di dalam blok `if` untuk keputusan bertahap.
2. **Perulangan `for` & `range()`**: Mengulang instruksi dengan urutan angka (rentang awal, akhir, dan langkah/*step*).
3. **Perulangan `while`**: Eksekusi blok kode berulang selama kondisi bernilai `True`.
4. **Pengendali Perulangan**:
   - `break` : Menghentikan perulangan seketika.
   - `continue` : Melewati sisa baris pada iterasi saat ini dan lanjut ke iterasi berikutnya.

### Rincian File:
- **Modul Praktikum:**
  - `latihan1.py` : Percabangan bertingkat syarat usia nonton film 17+ dan diskon kartu pelajar.
  - `latihan2.py` : Perulangan `for` dengan fungsi `range()` (hitung angka 1–5 dan tabel perkalian 3).
  - `latihan3.py` : Perulangan `while` untuk menjumlahkan angka berulang hingga pengguna menginput `0`.
  - `latihan4.py` : Penggunaan instruksi `break` (berhenti di angka 8) dan `continue` (menyaring bilangan ganjil).
  - `studi_kasus.py` : Rekap Nilai Kuis Kelas (validasi rentang nilai 0–100, pengelompokan bertingkat, rata-rata, nilai tertinggi, dan terendah).
- **Task Mandiri:**
  - `task1.py` : Percabangan bertingkat tiket bioskop dan diskon pelajar.
  - `task2.py` : Perhitungan total harga sepatu dengan perulangan `for`.
  - `task3.py` : Variasi `range(1, 10, 2)` dengan *step* dan loop `while` dasar.
  - `task4.py` : Simulasi mekanisme *do-while* di Python menggunakan pola `while True` + `break`.
  - `task5.py` : Program logika FizzBuzz (perulangan angka 1–29 dengan kondisi kelipatan 3 dan 5).

---

## 📌 Week 3: Pola Perulangan (Penelusuran, Kondisi Batas, dan Sentinel)

Fokus pada verifikasi logika perulangan, penanganan data tidak terduga, dan pencegahan galat algoritma.

### Materi Utama:
1. **Tabel Penelusuran (*Trace Table*)**: Mencatat perubahan variabel tiap putaran tanpa menjalankan program untuk mendeteksi *bug*.
2. **Jaminan Berhenti & Kondisi Batas**: Memastikan kondisi mencapai terminasi dan mencegah kesalahan *off-by-one* (`<` vs `<=`).
3. **Masukan Berpenanda (*Sentinel*)**: Pola pembacaan data dua kali menggunakan penanda (misal `-1`) saat jumlah data belum diketahui di awal.
4. **Pola Akumulator & Pencacah**: Mengumpulkan total nilai (`total = total + x`) dan menghitung frekuensi kejadian (`banyak = banyak + 1`).

### Rincian File:
- **Modul Praktikum:**
  - `latihan1.py` : Tabel penelusuran `while` loop penjumlahan kelipatan 2 (`total = 30`).
  - `latihan2.py` : Analisis dan perbaikan kondisi batas dari `i < n` menjadi `i <= n`.
  - `latihan3.py` : Input durasi mesin berpenanda (*sentinel* `-1`) dengan proteksi `ZeroDivisionError` pada data kosong.
  - `latihan4.py` : Pengolahan data produksi 10 hari terhadap target 50 unit menggunakan akumulator dan pencacah.
- **Task Mandiri:**
  - `task1.py` : Implementasi tabel penelusuran perulangan `while`.
  - `task2.py` : Uji coba penanganan kondisi batas penjumlahan angka 1 sampai $n$.
  - `task3.py` : Program masukan berpenanda sentinel durasi mesin dan perhitungan rata-rata.
  - `task4.py` : Rekapitulasi target produksi harian menggunakan pola akumulator dan pencacah.

---

## 📌 Week 4: Pengolahan Data Lanjut (Penyaringan, Nilai Ekstrem, dan Studi Kasus)

Fokus pada penerapan pola algoritma terpadu untuk pengolahan data riil dan pemecahan masalah kompleks.

### Materi Utama:
1. **Pola Penyaringan (*Filtering*)**: Mengintegrasikan struktur `if` di dalam loop agar hanya data yang memenuhi kriteria yang diproses.
2. **Pola Nilai Ekstrem & Jebakan Inisialisasi**: Mencari nilai maksimum/minimum secara aman (menghindari inisialisasi `0` yang berisiko pada data bertanda negatif dengan memakai `None`).
3. **Dekomposisi Masalah**: Mengurai masalah komputasi besar menjadi sub-masalah pola dasar (akumulator, pencacah, penyaring, ekstrem).

### Rincian File:
- **Modul Praktikum:**
  - `latihan1.py` : Pola penyaringan data produksi harian yang hanya mencapai target ($\ge 50$ unit).
  - `latihan2.py` : Pencarian laba bulanan tertinggi dengan inisialisasi aman `None` dan pelacakan bulan kejadian.
  - `latihan3.py` : Pencatatan suhu mesin 8 kali dengan gabungan nilai ekstrem tertinggi, pencacah suhu $> 80^\circ$, dan rata-rata suhu tersaring.
  - `studi_kasus.py` : Rekap Produksi Lini Perakitan (sentinel `-1`, target 100 unit, pencarian hari tertinggi & terendah, dan rata-rata produksi khusus hari target).
- **Task Mandiri:**
  - `task1.py` : Program penyaringan data produksi harian mencapai target.
  - `task2.py` : Program penentuan nilai ekstrem laba tertinggi beserta periode bulannya.
  - `task3.py` : Pengelompokan dan dekomposisi masalah analisis suhu mesin.
  - `task4.py` : Program terintegrasi studi kasus produksi harian lini perakitan.

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
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   └── task5.py
├── Week-2/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   ├── studi_kasus.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   └── task5.py
├── Week-3/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── latihan4.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
├── Week-4/
│   ├── latihan1.py
│   ├── latihan2.py
│   ├── latihan3.py
│   ├── studi_kasus.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
└── Readme.md
```

---

## 🚀 Cara Menjalankan Kode

1. Buka terminal atau Command Prompt / PowerShell.
2. Masuk ke direktori folder week yang ingin dijalankan:
   ```bash
   cd Week-1
   ```
3. Jalankan file program menggunakan interpreter Python:
   ```bash
   python latihan1.py
   # atau
   python task1.py
   ```
