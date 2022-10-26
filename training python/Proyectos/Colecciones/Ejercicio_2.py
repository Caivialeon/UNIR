#Ejercicio 2

lista1= set([0,1,2,3,4,5])
lista2= set([5,6,7,8,9,0])
#lista = list(set(lista))
lista3= list(lista1 | lista2)
lista4= list(lista2 - lista1)
lista5= list(lista1 - lista2)
lista6= list(lista1 ^ lista2)

print(lista3)
print(lista4)
print(lista5)
print(lista6)