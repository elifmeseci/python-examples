"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem : ax^2 + bx + c

Delta : b^2-4ac
1.kök : (-b - delta^0.5) / (2a)
2.kök : (-b + delta^0.5) / (2a)
"""
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta = b**2-4*a*c
x1 = (-b - delta **0.5) / (2*a)
x2 = (-b + delta **0.5) / (2*a)

print("Birinci kökünüz: {}\nİkinci kökünüz: {}\n".format(x1,x2))