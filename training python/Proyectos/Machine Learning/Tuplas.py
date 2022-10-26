#Tupla
'''
Tupla = (1,2,3,4,5,6)
print(Tupla)
Tupla[0] = 50

print(Tupla)
'''

tupla_a = (1,2,3,4)
tupla_b = ("uno","dos","tres")
print(tupla_a+tupla_b)

tupla_c = ("python ")*4
print(tupla_c)

tupla_d =(1,5,2,3,5,4,5)
repetido = tupla_d.count(5)
print(repetido)
repetido = tupla_d.index(5)
print(repetido)

#modificar tuplas por medio de listas y conversiones.

x = ("rojo","amarillo","verde")
print(x)
y = list (x)
y[1] = "azul"
x = tuple(y)
print(x)


