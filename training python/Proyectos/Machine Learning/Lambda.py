#lambda es una funcion anomina.

doble = lambda x:x *2
print(doble(30))

lista = [1,23,3,5,6,5,78,966]
lista_pares = list (filter(lambda x: (x%2 == 0),lista))

print(lista_pares)

lista2 = [1,23,3,5,6,5,78,966]
lista_doble = list (map(lambda x:x*2,lista2))
print(lista_doble)