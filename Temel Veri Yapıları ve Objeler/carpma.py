#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapın.

print("Çarpma işlemi için üç sayı girin:\n")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

çarpım = a*b*c
print("{} x {} x {} = {} ".format(a,b,c,çarpım))
