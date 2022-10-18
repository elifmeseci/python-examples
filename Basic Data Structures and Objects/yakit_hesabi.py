"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve
sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = int(input("Kaç km yol yaptınız:"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))