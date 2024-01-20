#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

import math
denominador=2
diferencia=1
euler = 2
antfra = 1
fraccion = 1
while diferencia>0.0001:
    antfra = fraccion
    fraccion= 1/math.factorial(denominador)
    denominador += 1
    euler += fraccion
    diferencia= antfra-fraccion
print(euler)