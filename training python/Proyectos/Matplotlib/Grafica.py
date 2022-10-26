import matplotlib.pyplot as plt
import numpy as np

arrayX = np.array([1,2,3,4,5,6])
arrayY = np.array([6,5,4,3,2,1])

array2X = np.random.randint(low=1 , high= 100 , size = 10)
array2Y = np.random.randint(low=1 , high= 100 , size = 10)

plt.plot(arrayX,arrayY,"pb")
plt.ylabel("Eje y")
plt.xlabel("Eje x")

plt.plot(array2X , array2Y)
plt.show()


