#crear una lista a partir de otra.
'''
curso  = []
for letras in "python":
    curso.append(letras)
print(curso)

curso = [letras for letras in "python"]
print(curso)


lista_a = [1,2,3,4,5,6]
lista_b = []

for i in lista_a:
    para_lista_b = i * 2
    lista_b.append(para_lista_b)
print(lista_b)
'''

lista_a = [1,2,3,4,5,6]
lista_b = [i*2 for i in lista_a]
print(lista_b)