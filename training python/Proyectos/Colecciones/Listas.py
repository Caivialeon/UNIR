#listas o arreglos

#lista = ["lunes","martes","miercoles","jueves","viernes",1,2,3,True,[1,2,3,"n"]]
'''
lista =[1,2,3,4,5,"Aldo"]

print("alberto" in lista)
'''
'''lista1 = [1,2,3,4,5]
la lista empieza con el 0
lista.remove(1)elimina el valor que se quiere eliminar.
lista.sort(reverse = true)  <- ordena 
lista.clear()
lista.reverse() <-- voltea todos los elementos
lista2 = [6,7,8]
lista3 = lista1+lista2
lista.pop()  <-- elimina el ultimo valor de la lista
lista.pop(3)
#lista.append(6)
#lista.insert(2,"aldo")
#lista.extend([6,7,8,9,10])'''
#print(lista3)
#print(len(lista))
import random
import math

def ejercicio3(lista):
    lista2 = []
    for i in lista :
        i = round(i)
        lista2.append(i)
    lista = lista2
    return lista2

def ejercicio2(lista , x ):
    lista2 = []
    for i in lista :
        i/=x
        lista2.append(i)
    lista = lista2
    return lista2

def ejercicio5(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2

from math import factorial
from math import gcd

def ejercicio4( x , y):
    x = factorial(x)
    y = gcd(x,y)
    tupla = x , y
    return tupla
lista = list( random.sample(range(1, 100), 15))

lista2 = ejercicio2(lista , 3)
lista3 = ejercicio3(lista2)
lista5 = ejercicio5(lista)
print(lista)
print(lista2)
print(lista3)
print(lista5)
print (ejercicio4(2,8))

'''
x = [72, 50, 81, 74, 94, 86, 59, 83, 65, 33, 88, 81]
x_=[]
for i in x:
    i/=10   #Procesa los datos uno por uno
    x_.append(i)
x=x_
print(x)'''