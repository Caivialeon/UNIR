import numpy as np
'''
m = np.random.randint(10, size = (3,3))
m1 = np.random.rand(5)
m2 = np.random.choice([3,5,9,5,1], size = (3,3))
print(m)
print(m1)
print(m2)
'''
#probabilidad de 2 dados salgan pares.
m2 = np.random.choice([2,4,6], p = [0.4,0.4,0.2] , size = (100))
print(m2)
#matriz que contenga 50 valores , donde cada valor debe ser 4,2,8 0 10
m3 = np.random.choice([2,4,6,8,10] , p = [.2,.2,.2,.2,.2] , size = [50])
print(m3)