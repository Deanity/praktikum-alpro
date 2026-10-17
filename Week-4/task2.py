tertinggi = None
bulan_tertinggi = None

for bulan in range(1, 7):
    laba = int(input(f"Laba bulan {bulan} (juta): "))
    if tertinggi is None or laba > tertinggi:
        tertinggi = laba
        bulan_tertinggi = bulan

print(f"Laba tertinggi: {tertinggi} juta (bulan ke-{bulan_tertinggi})")
