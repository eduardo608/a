#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

n = int(input("n: "))
suma=0
for i in range(n):
    suma+=(-1)**(i)*(1/(2*i+1))
pi = 4 * suma
print(pi)