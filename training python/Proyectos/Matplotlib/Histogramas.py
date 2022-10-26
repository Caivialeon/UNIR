import matplotlib.pyplot as plt
import numpy as np

arrayX = np.array([1,2,3,4,5,6])
arrayY = np.array([6,5,4,3,2,1])

array2X = np.random.randint(low=1 , high= 100 , size = 10)
array2Y = np.random.randint(low=1 , high= 100 , size = 10)

#plt.hist2d(array2Y , array2X, orientation="horizontal", color="gray")
#plt.hist2d(array2Y , array2X)
"""
plt.ylabel("Eje y")
plt.xlabel("Eje x")
plt.show()
"""

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
values_x= ["a", "b", "c" , "d" , "e"]
values_y = [1,5,6,7,8]
ax.bar(values_x, values_y)
plt.show()

