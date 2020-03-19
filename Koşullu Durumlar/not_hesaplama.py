"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
print("Lütfen vize1,vize2,final notlarınızı giriniz.\n")
vize1 = float(input("Vize1: "))
vize2 = float(input("Vize2: "))
final = float(input("Final: "))
ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if ortalama >= 90:
    print("{} :AA".format(ortalama))
elif ortalama >= 85:
    print("{} :BA".format(ortalama))
elif ortalama >= 80:
    print("{} :BB".format(ortalama))
elif ortalama >= 75:
    print("{} :CB".format(ortalama))
elif ortalama >= 70:
    print("{} :CC".format(ortalama))
elif ortalama >= 65:
    print("{} :DC".format(ortalama))
elif ortalama >= 60:
    print("{} :DD".format(ortalama))
elif ortalama >= 55:
    print("{} :FD".format(ortalama))
elif ortalama < 55:
    print("{} :FF".format(ortalama))
