print("""
**************************************
Atm Makinesine Hoşgeldiniz
İşlemler:
1-Bakiye Sorgulama
2-Para Yatırma
3-Para Çekme
Programdan çıkmak için 0 a basınız.
***************************************""")
bakiye = 1000
while True:
    islem = input("İşlemi seçiniz")
    if islem == "0":
        print("Yine bekleriz.")
        break
    elif islem == "1":
        print("Bakiyeniz {} tldir".format(bakiye))
    elif islem == "2":
        miktar = int(input("Yatıracağınız miktarı giriniz: "))
        bakiye += miktar
    elif islem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if miktar > bakiye:
            print("Bakiyeniz yetersiz...")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem...")