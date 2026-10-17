print("Bilangan ganjil dari 1 sampai 10 (berhenti jika bertemu 8)")
for i in range(1, 11):
    if i == 8:
        break
    if i % 2 == 0:
        continue
    print(i)
print("Perulangan selesai")
