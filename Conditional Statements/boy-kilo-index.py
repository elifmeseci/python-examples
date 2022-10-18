"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 BKİ 18.5'un altındaysa -------> Zayıf
 BKİ 18.5 ile 25 arasındaysa ------> Normal
 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
 BKİ 30'un üstündeyse -------------> Obez

Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)
"""
kilo = int(input("kilonuz: "))
boy = float(input("boyunuz: "))
indeks = kilo/(boy**2)

if indeks < 18.5:
    print("Beden kitle indeksiniz: {}\nZayıf".format(indeks))
elif indeks> 18.5 and indeks < 25:
    print("Beden kitle indeksiniz: {}\nNormal".format(indeks))
elif indeks> 25 and indeks <30:
    print("Beden kitle indeksiniz: {}\nFazla Kilolu".format(indeks))
else:
    print("Beden kitle indeksiniz: {}\nObez".format(indeks))