#Ejercicio 4

import math

r= float(input("Ingresa el valor del Radio : "))

'''
area = 3.1416 * (r**2)
longitud = 2*3.1416*r
'''
area = math.pi * r**2
longitud = 2*math.pi*r

print(f"El valor del área es : {area:.2f}")
print(f"el valor de la longitud es : {longitud:.2f}")