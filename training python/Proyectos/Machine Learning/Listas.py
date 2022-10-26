#listas

lista = [1,2,3.5,"Aldo"]
print(lista)

lista[2] = "Alberto"
print(lista)
lista[-1] = 3
print(lista)
print(len(lista))
#cortar una lista
print(lista[1:3])
print(lista[1:])
#insertar
lista.insert(2,"nuevo")
print(lista)
lista.append("viejo")
print(lista)
print(lista.index(2))
#eliminar datos
print(lista.pop())
print(lista)
