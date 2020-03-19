"""
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir
dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir
üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın
"""
sekil = str(input("Geometrik şekiliniz üçgen mi dörtgen mi ?"))

if sekil == "dörtgen":
    print("Lütfen kenarları giriniz:\n")
    a = int(input("1. kenar: "))
    b = int(input("2. kenar: "))
    c = int(input("3. kenar: "))
    d = int(input("4. kenar: "))
    if (a == b and a == c and a == d):
        print("Girilen dörten, karedir.")
    elif (a == c and a == d and a != b):
        print("Girilen dörtgen, dikdörtgendir.")
    else :
        print("Girilen dörtgen sıradan bir dörtgendir.")

if sekil == "üçgen":
    print("Lütfen kenarları giriniz:\n")
    a = int(input("1. kenar: "))
    b = int(input("2. kenar: "))
    c = int(input("3. kenar: "))

    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Girilen üçgen, eşkenar üçgendir.")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Girilen üçgen, ikizkenar üçgendir.")
        else:
            print("Girilen üçgen, çeşitkenar üçgendir.")
    else:
        print("Girilen değerler üçgen belirtmiyor...")

else :
    print("Geçersiz Şekil...")