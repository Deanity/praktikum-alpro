def faktorial(n):
    if n == 0:
        return 1
    return n * faktorial(n - 1)


def hitung_mundur(n):
    if n == 0:
        print("Mulai!")
    else:
        print(n)
        hitung_mundur(n - 1)


print("5! =", faktorial(5))
hitung_mundur(3)
