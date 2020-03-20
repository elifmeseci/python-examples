from math import *
print("""
********************
Hesap Makinesi İşlemler
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Kök alma
6-Üssünü alma
7-faktoriyel hesaplama
8-logaritma hesaplama
9-Mod alma
10-Ebob hesaplama
**********************""")

a = int(input("Birinci sayıyı giriniz"))
b = int(input("İkinci sayıyı giriniz"))
islem = input("İşlemi giriniz")

if islem == "1":
    print("{} ile {} toplamı: {}".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} farkı: {}".format(a,b,a - b))
elif islem == "3":
    print("{} ile {} çarpımı: {}".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} bölümü: {}".format(a,b,a / b))
elif islem == "5":
    print("{}'nın kökü: {}".format(a,sqrt(a)))
elif islem == "6":
    print("{} ile {} üssü: {}".format(a, b, pow(a,b)))
elif islem == "7":
    print("{} faktoriyeli: {}".format(a, factorial(a)))
elif islem == "8":
    print("{} ile {} logaritması: {}".format(a, b, log(a, b)))
elif islem == "9":
    print("{} ile {} modu: {}".format(a, b, fmod(a,b)))
elif islem == "10":
    print("{} ile {} ebobu: {}".format(a, b,gcd(a,b)))
else:
    print("Geçersiz işlem...")