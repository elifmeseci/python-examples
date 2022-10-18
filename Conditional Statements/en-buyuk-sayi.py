#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

print("Üç sayı giriniz: \n")
a = int(input("birinci sayi: "))
b = int(input("ikinci sayi: "))
c = int(input("üçüncü sayi: "))

if a > b and a > c:
    print("En büyük sayı: {}".format(a))
elif b > a and b > c:
    print("En büyük sayı: {}".format(b))
elif (c >= a and c >= b):
    print("En büyük sayı: {}".format(c))