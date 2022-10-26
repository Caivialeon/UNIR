import numpy as np

m = np.array([[1,-1,2],[3,2,0]])
print(m)
print("")
#Matriz traspuesta
m1 = np.array([[1],[2],[3]])
print(np.transpose(m1))
#sistema de ecuacion
#ax=b
#matriz a
a = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
#matriz b
b = np.array([[-3],[5],[-2]])
print(np.transpose(b))
print("")
#encontrar x
x = np.linalg.solve(a,b)
print(x)
print("")
print(np.allclose(np.dot(a,x),b))

#sistema de ecuaciones
'''
2x+7y+3z = 1
2x+8y+2z = 1
x+3y+z=0
'''

m2 = np.array([[2,7,3],[2,8,2],[1,3,1]])
m3 = np.array([[1],[1],[0]])
print(np.linalg.solve(m2,m3))

