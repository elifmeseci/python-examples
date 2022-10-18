"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
kilo = int(input("kilonuz: "))
boy = float(input("boyunuz: "))
indeks = kilo/(boy**2)

print("Beden kitle indeksiniz: {}".format(indeks))