print("""
********************
Hesap Makinesi İşlemler
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
**********************""")

a = int(input("Birinci sayıyı giriniz"))
b = int(input("İkinci sayıyı giriniz"))
islem = input("İşlemi giriniz")

if islem == "1":
    print("{} ile {} toplamı: {}".format(a,b,a + b))
elif islem == "2":
    print("{} ile {} farkı: {}".format(a,b,a - b))
elif islem == "3":
    print("{} ile {} çarpımı: {}".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} bölümü: {}".format(a,b,a / b))
else:
    print("Geçersiz işlem...")