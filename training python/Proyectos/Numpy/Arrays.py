#Arrays solo consta de elementos que pertenecen al mismo tipo de datos.
#listas no puede manejar operaciones aritmeticas directamente.
#Arrays puede manejar directamente operaciones aritmeticas.

'''
import array as ar
import numpy as np

matriz = ar.array("i",[1,2,3,4,5])
print(matriz)

for ar in matriz:
    print(ar)
'''
import numpy as np

matriz = np.array([1,2,3,4,5])
print(matriz)

lista = [1,3,5]
matriz = np.array([2,4,6])
lista.append(7)
matriz = matriz + np.array([8])
print(lista)
print(matriz)





