"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
a = int(input("kenar a: "))
b = int(input("kenar b: "))

hipotenus = (a**2 +b**2)**0.5
print("üçgenin hipotenüsü : {}".format(hipotenus))