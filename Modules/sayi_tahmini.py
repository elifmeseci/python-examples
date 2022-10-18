import random
import time

print("""
 Sayı Tahmini Oyunu
 1 ile 40 arasında bir sayı tahmin edin.""")

rasgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:
    tahmin = int(input("Tahmininiz: "))
    if tahmin < rasgele_sayi :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı tahmin edin.")
        tahmin_hakki -= 1
    elif tahmin > rasgele_sayi :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı tahmin edin.")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayı:",rasgele_sayi)
        break
    if tahmin_hakki == 0 :
        print("Tahmin hakkınız bitmiştir...")
        print("Sayı:", rasgele_sayi)