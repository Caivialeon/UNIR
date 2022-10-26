import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print("")
#maximos y minimos
print(np.amin(m,0))
print("")
#Rango es la resta del valor maximo y minimo
print(np.ptp(m , axis = 1))
print("")
#perceptibles  = q(n+1)/100
print(np.percentile(m,50))
print("")
#mediana
print(np.median(m , axis = 0))
print("")
#media aritmetica
print(np.mean(m))
print("")
#promedio ponderado
m1 = np.array([1,2,3,4,5,6])
print(np.average(m1))
print("")
#desviacion estandar
print(np.std(m1))