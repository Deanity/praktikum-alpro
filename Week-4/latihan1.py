TARGET = 50
HARI = 10

total_lolos = 0
banyak_lolos = 0

for hari in range(1, HARI + 1):
    produksi = int(input(f"Produksi hari ke-{hari}: "))
    if produksi >= TARGET:
        total_lolos = total_lolos + produksi
        banyak_lolos = banyak_lolos + 1

if banyak_lolos == 0:
    print("Tidak ada hari yang mencapai target.")
else:
    rata = round(total_lolos / banyak_lolos, 2)
    print("Hari mencapai target:", banyak_lolos)
    print("Total unit pada hari tersebut:", total_lolos)
    print("Rata-rata unit pada hari tersebut:", rata)
