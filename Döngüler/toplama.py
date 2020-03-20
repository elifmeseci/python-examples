"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""
toplam = 0
while True:
    sayi = input("Sayı:")
    if sayi == "q":
        break
    sayi = int(sayi)
    toplam += sayi
print("Toplam: ",toplam)