"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayi = (input("Bir sayı giriniz:"))
basamak_sayisi = len(sayi)
sayi = int(sayi)
toplam = 0
basamak = 0
temp = sayi

while (temp > 0):
    basamak = temp % 10

    toplam += basamak ** basamak_sayisi

    temp //= 10

if (toplam == sayi):
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")
