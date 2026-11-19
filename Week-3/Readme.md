# Laporan Praktikum Week 3 — Pola Perulangan: Penelusuran, Penanda, dan Pengolahan Data (Bagian 1)

## Identitas Diri
```py
Nama  = "Dendra De Tama"
NIM   = 108052600034
Kelas = "SS1SI-50-REG-01"
Dosen = "Adzanil Rachmadhi Putra"
```

---

## Deskripsi Program

Praktikum Week 3 berfokus pada teknik analisis, verifikasi, dan perancangan pola dasar perulangan Python 3 sesuai Modul Praktikum 3 Bagian 1. Pembahasan berfokus pada keandalan logika struktur perulangan melalui **tabel penelusuran (*trace table*)**, **analisis jaminan berhenti (*termination guarantee*)**, **pencegahan kesalahan satu putaran (*off-by-one error*)**, serta **pola masukan berpenanda (*sentinel loop*)** dan **pola akumulator-pencacah dasar**.

Kumpulan program yang diimplementasikan pada pertemuan Week 3 meliputi:
1. `latihan1.py`: Program kalkulasi penjumlahan kelipatan dua dari rentang $n = 1$ hingga $5$ menggunakan perulangan `while`, diverifikasi menggunakan tabel penelusuran langkah demi langkah untuk melacak perubahan nilai `n` dan `total`.
2. `latihan2.py`: Program penjumlahan deret bilangan 1 sampai $n$ yang merefleksikan identifikasi kesalahan *off-by-one* (perbedaan kondisi `<` vs `<=`) serta verifikasi kondisi batas ($n = 5$, $n = 1$, dan $n = 0$).
3. `latihan3.py`: Program penghitung rata-rata waktu proses mesin berbasis nilai penanda (*sentinel*) `-1` dengan menerapkan pola baca ganda (*read-twice pattern*) serta proteksi penanganan data kosong (*zero-division guard*).
4. `latihan4.py`: Program rekapitulasi data produksi harian lini pabrik selama 10 hari yang mengintegrasikan pola akumulator (`total`) dan pola pencacah bersyarat (`di_bawah`) terhadap target harian.

---

## Dekomposisi Masalah

| Sub-Masalah | Plan Pemrograman | Letak di Program | Keterangan |
| :--- | :--- | :--- | :--- |
| **Penelusuran State Perulangan** | *Trace Table Verification* | `latihan1.py`, baris 4–6 | Menelusuri transisi variabel pengontrol `n` dan akumulator `total` tiap iterasi. |
| **Pembaruan Nilai Melangkah (*Step*)** | Operasi Penambahan Monotonik | `latihan1.py`, baris 6 | Pernyataan `n = n + 1` menjamin kondisi `n <= 5` suatu saat bernilai `False`. |
| **Koreksi Batas Atas Deret** | *Inclusive Boundary Guard (`<=`)* | `latihan2.py`, baris 5 | Memastikan nilai batas atas $n$ ikut diproses, mencegah hilangnya iterasi terakhir. |
| **Penanganan Batas Nol (*Boundary Case*)** | Evaluasi Kondisi Awal Instan | `latihan2.py`, baris 5, 9 | Menjamin masukan $n = 0$ langsung mengabaikan blok perulangan tanpa memicu galat. |
| **Pola Pembacaan Ganda (*Read-Twice*)** | *Pre-read & Loop-end Read Pattern* | `latihan3.py`, baris 4, 9 | Membaca sebelum loop dan di akhir blok agar nilai sentinel `-1` tidak ikut terproses sebagai data. |
| **Penghitungan Frekuensi Kejadian** | *Counter Pattern* | `latihan3.py`, baris 8 | Menambahkan pencacah `banyak = banyak + 1` setiap ada durasi yang sah. |
| **Pencegahan Galat Pembagian Nol** | *Zero-Division Guard Condition* | `latihan3.py`, baris 11–15 | Mengevaluasi `if banyak == 0:` sebelum menghitung rata-rata `total / banyak`. |
| **Pembulatan Presisi Rata-Rata** | Fungsi Intrinsik `round()` | `latihan3.py`, baris 15 | Memformat presisi nilai desimal rata-rata hingga dua digit di belakang koma. |
| **Akumulasi Kuantitas Produksi** | *Accumulator Pattern* | `latihan4.py`, baris 9 | Menjumlahkan unit produksi harian ke dalam variabel `total`. |
| **Pencacahan Ambang Batas** | *Conditional Counter Filtering* | `latihan4.py`, baris 10–11 | Mencacah hari yang produksinya di bawah batas target (`produksi < TARGET`). |
| **Kalkulasi Rata-Rata Terdistribusi** | Operasi Pembagian Skalar Konstan | `latihan4.py`, baris 14 | Menghitung rata-rata harian dengan membagi akumulator terhadap konstanta `HARI`. |

---

## Flowchart & Pseudocode

### Flowchart Masukan Berpenanda & Proteksi Data Kosong (`latihan3.py`)

```mermaid
flowchart TD
    A([Mulai]) --> B["Inisialisasi: total = 0, banyak = 0"]
    B --> C["Input durasi (pertama)"]
    C --> D{durasi != -1?}
    D -- Ya --> E["total = total + durasi"]
    E --> F["banyak = banyak + 1"]
    F --> G["Input durasi (berikutnya)"]
    G --> D
    D -- Tidak --> H{banyak == 0?}
    H -- Ya --> I["Tampilkan 'Belum ada data yang dimasukkan.'"]
    H -- Tidak --> J["Hitung rata_rata = round(total / banyak, 2)"]
    J --> K["Tampilkan Banyak data dan Rata-rata"]
    I --> L([Selesai])
    K --> L
```

---

### Pseudocode `latihan2.py` (Koreksi Kondisi Batas Penjumlahan 1 s.d. n)

```text
ALGORITMA PenjumlahanDeret
MASUKAN : n : INTEGER
KELUARAN: total : INTEGER

DEKLARASI:
    n, total, i : INTEGER

PROSES:
    BACA n
    total <- 0
    i <- 1

    SELAMA i <= n LAKUKAN
        total <- total + i
        i <- i + 1
    AKHIR SELAMA

    TAMPILKAN "Jumlah:", total
SELESAI
```

---

### Pseudocode `latihan4.py` (Akumulator & Pencacah Produksi Harian)

```text
ALGORITMA RekapProduksiTarget
MASUKAN : produksi (setiap hari ke-1 s.d. 10) : INTEGER
KELUARAN: total, rata_rata, di_bawah

DEKLARASI:
    KONSTANTA TARGET = 50
    KONSTANTA HARI = 10
    total, di_bawah, hari, produksi : INTEGER
    rata_rata : FLOAT

PROSES:
    total <- 0
    di_bawah <- 0

    UNTUK hari DARI 1 SAMPAI HARI LAKUKAN
        BACA produksi
        total <- total + produksi
        JIKA produksi < TARGET MAKA
            di_bawah <- di_bawah + 1
        AKHIR JIKA
    AKHIR UNTUK

    rata_rata <- total / HARI

    TAMPILKAN "Total produksi:", total
    TAMPILKAN "Rata-rata per hari:", rata_rata
    TAMPILKAN "Hari di bawah target:", di_bawah
SELESAI
```

---

## Tabel Penelusuran (Trace Table)

### 1. Tabel Penelusuran `latihan1.py`
Kode program: `total = 0; n = 1; while n <= 5: total = total + n * 2; n = n + 1`

| Pemeriksaan ke- | Nilai `n` | Kondisi `n <= 5` | Ekspresi `n * 2` | `total` (sebelumnya + tambah) | `n` sesudah pembaruan |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | **True** | 2 | $0 + 2 = 2$ | 2 |
| 2 | 2 | **True** | 4 | $2 + 4 = 6$ | 3 |
| 3 | 3 | **True** | 6 | $6 + 6 = 12$ | 4 |
| 4 | 4 | **True** | 8 | $12 + 8 = 20$ | 5 |
| 5 | 5 | **True** | 10 | $20 + 10 = 30$ | 6 |
| 6 | 6 | **False** | - | Perulangan Berhenti | 6 |

*Hasil Akhir*: `total = 30` (Kondisi diperiksa **6 kali**, menghasilkan **5 kali iterasi sukses**).

---

### 2. Tabel Komparasi Kondisi Batas `latihan2.py` ($n = 5$)

Perbandingan antara kode awal dengan bug (`i < n`) dan kode setelah koreksi (`i <= n`):

| Pemeriksaan ke- | Nilai `i` | Kondisi Awal `i < 5` | `total` (Bug) | Kondisi Perbaikan `i <= 5` | `total` (Valid) | Keterangan |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 1 | True | 1 | True | 1 | $0 + 1$ |
| 2 | 2 | True | 3 | True | 3 | $1 + 2$ |
| 3 | 3 | True | 6 | True | 6 | $3 + 3$ |
| 4 | 4 | True | 10 | True | 10 | $6 + 4$ |
| 5 | 5 | **False (Macet)** | **10 (Salah)** | **True** | **15 (Benar)** | Pada kode awal, $i = 5$ terlewat |
| 6 | 6 | - | - | **False (Selesai)**| 15 | Berhenti pada batas yang tepat |

---

### 3. Tabel Penelusuran Sentinel `latihan3.py`
Masukan urut: `12`, `15`, `10`, `-1`

| Langkah | Masukan `durasi` | Evaluasi `durasi != -1` | `total` Kumulatif | `banyak` Data | Status Pembacaan |
| :---: | :---: | :---: | :---: | :---: | :--- |
| Pembacaan 1 | 12 | True | $0 + 12 = 12$ | 1 | Data valid ke-1 |
| Pembacaan 2 | 15 | True | $12 + 15 = 27$ | 2 | Data valid ke-2 |
| Pembacaan 3 | 10 | True | $27 + 10 = 37$ | 3 | Data valid ke-3 |
| Pembacaan 4 | -1 | **False** | 37 (tetap) | 3 (tetap) | Sentinel terdeteksi $\to$ loop henti |
| **Output Akhir** | - | Evaluasi `banyak == 0` $\to$ **False** | Rata-rata $= 37 / 3 = \mathbf{12.33}$ | **Banyak: 3** | **Sesuai Ekspektasi** |

---

## Tabel Kasus Uji

| No | Program | Kategori Uji | Masukan (*Input*) | Hasil yang Diharapkan (*Expected*) | Hasil Aktual Program (*Actual*) | Status |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | `latihan1.py` | **Normal** | Loop otomatis ($n=1..5$) | `total = 30` | `total = 30` | PASS |
| 2 | `latihan2.py` | **Normal** | $n = 5$ | `Jumlah: 15` | `Jumlah: 15` | PASS |
| 3 | `latihan2.py` | **Batas Bawah** | $n = 1$ | `Jumlah: 1` | `Jumlah: 1` | PASS |
| 4 | `latihan2.py` | **Batas Nol** | $n = 0$ | `Jumlah: 0` (langsung lewati loop) | `Jumlah: 0` | PASS |
| 5 | `latihan3.py` | **Normal** | 12, 15, 10, -1 | Banyak data: 3, Rata-rata: 12.33 menit | Sesuai output modul | PASS |
| 6 | `latihan3.py` | **Data Kosong** | Langsung memasukkan `-1` | "Belum ada data yang dimasukkan." | Sesuai output modul | PASS |
| 7 | `latihan4.py` | **Normal** | 48, 52, 39, 61, 55, 44, 58, 36, 63, 50 | Total produksi: 506<br>Rata-rata per hari: 50.6<br>Hari di bawah target: 4 | Sesuai output modul | PASS |
| 8 | `latihan4.py` | **Variasi Target**| TARGET = 55 (data sama) | Hari di bawah target: 6 | Sesuai ekspektasi modul | PASS |

---

## Catatan Pertanyaan Modul & Analisis Galat

### Jawaban Pertanyaan Praktik Modul:
1. **Latihan 1 (Langkah 5)**: Berapa kali kondisi diperiksa pada program awal (`n <= 5`) dan pada program yang sudah diubah (`n < 5`)?
   - *Jawaban*: Pada program awal (`n <= 5`), kondisi diperiksa sebanyak **6 kali** (5 kali True, 1 kali False menghentikan perulangan; total = 30). Pada program yang diubah (`n < 5`), kondisi diperiksa sebanyak **5 kali** (4 kali True, 1 kali False saat $n=5$; total = 20).
2. **Latihan 2 (Langkah 6)**: Mengapa $n = 0$ menghasilkan 0 dan bukan pesan galat?
   - *Jawaban*: Karena variabel pengontrol diinisialisasi `i = 1`. Saat pertama kali dievaluasi pada `while i <= 0:`, perbandingan langsung bernilai `False`. Akibatnya, badan perulangan tidak pernah dimasuki sama sekali dan program langsung mencetak nilai awal `total` yaitu `0`.
3. **Latihan 3 (Langkah 5)**: Mengapa memindahkan baris input ke awal blok `while` membuat banyak data dan rata-ratanya berbeda?
   - *Jawaban*: Data pertama (12) langsung tertimpa oleh data kedua (15) sebelum sempat ditambahkan ke `total` dan `banyak`. Selain itu, saat pengguna mengetik nilai penanda `-1`, nilai `-1` tersebut terbaca di baris pertama blok dan ikut diakumulasikan ke dalam `total` serta menambah pencacah `banyak` sebelum kondisi `while` sempat memeriksa dan menghentikannya.
4. **Latihan 4 (Langkah 5)**: Variabel mana yang berperan sebagai akumulator dan variabel mana yang berperan sebagai pencacah?
   - *Jawaban*: Variabel `total` berperan sebagai **akumulator** (menjumlahkan nilai data produksi tiap hari: `total = total + produksi`), sedangkan variabel `di_bawah` berperan sebagai **pencacah** (menghitung banyaknya kejadian dengan selalu menambah satu: `di_bawah = di_bawah + 1`).

### Analisis Galat Teknis:
1. **Galat Kesalahan Satu Putaran (*Off-by-One Logic Error*)**:
   - *Penyebab*: Penggunaan operator `<` alih-alih `<=` pada `while i < n:` di `latihan2.py`.
   - *Perbaikan*: Mengubah kondisi menjadi inklusif `while i <= n:`.
2. **Galat Pembagian Nol (*ZeroDivisionError*)**:
   - *Penyebab*: Membagi `total / banyak` saat tidak ada data yang dimasukkan (langsung input `-1`).
   - *Perbaikan*: Memasang *guard condition* `if banyak == 0:`.

---

## Refleksi

Praktikum Week 3 membuktikan bahwa sintaks yang valid secara teknis belum tentu menjamin kebenaran logika algoritma. Pembuatan tabel penelusuran (*trace table*) di atas kertas sangat efektif untuk mendeteksi *off-by-one error* dan memahami kapan evaluasi terakhir bernilai `False`.

Penerapan pola masukan berpenanda (*sentinel*) dengan metode baca ganda (*read-twice*) memberikan solusi yang aman untuk memproses data tanpa mengetahui ukurannya di awal, sekaligus menjamin penanda tidak ikut dihitung ke dalam data agregasi.

---

## Pengungkapan Penggunaan AI

- **Bagian yang Dibantu AI**:
  - Format tabel penelusuran (*trace table*) dan tabel komparasi kondisi batas $i < n$ vs $i \le n$.
  - Perancangan diagram alir Mermaid untuk pola baca ganda masukan berpenanda.
  - Penataan jawaban sistematis terhadap pertanyaan panduan dari Modul Praktikum 3.
- **Saran AI yang Dipakai**:
  - Penambahan visualisasi alur proteksi data kosong (`banyak == 0`) pada pseudocode dan flowchart `latihan3.py`.
  - Format pengujian boundary value analysis ($n=5, n=1, n=0$).
- **Saran AI yang Ditolak & Alasannya**:
  - Penggunaan `sum()` atau `range()` untuk menyederhanakan `latihan2.py`, ditolak agar tetap melatih logika manual algoritma perulangan `while`.
