#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

print("iki sayı giriniz: \n")
a= int(input("birinci sayi: "))
b= int(input("ikinci sayi: "))

a,b = b,a
print("Birinci sayi: {}\nİkinci sayi: {}".format(a,b))
