import numpy as np

matriz = np.array([1,2,3,4,5,6])
print(matriz)
#matriz de 2d
m2d = np.array([[1,2,3],[4,5,6]])
print(m2d)

lista = [1,2,3,4,5]
matriz2 = np.array(lista)
print(matriz2)

#forma rapida de crear array 2d

m = np.arange(15).reshape(3,5)
print(m)