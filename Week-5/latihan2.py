def celciuskefarenhit(c):
    return c * 9 / 5 + 32

def luaspersegipanjang(p, l):
    return p * l 

suhu = float(input("Masukkan Suhu (C)"))
f = celciuskefarenhit(suhu)
print("Farenhit: ", f)

luaskamar = luaspersegipanjang(3,4)
print(luaskamar)

luasdapur = luaspersegipanjang(6,5)
print(luasdapur)

print("Total luas: ", luasdapur + luaskamar)