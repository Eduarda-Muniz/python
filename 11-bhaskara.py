import math 

a = float(input ("digite o valor do coeficiente A: "))
b = float(input ("digite o valor do coeficiente B: "))
c = float(input ("digite o valor do coeficiente C: "))

delta = b**2 - 4*a*c

if delta < 0:
    print (f"a equação não possui raízes reais.")
elif delta == 0:

    raiz_unica = -b / ( 2 * a)
    print (f"a equação possui uma única raiz real: {raiz_unica:2f}")
else:
     
    raiz1 = (-b + math.sqrt(delta) / 2 * a)
    raiz2 = (-b - math.sqrt(delta) / 2 * a)
    print (f" a equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
