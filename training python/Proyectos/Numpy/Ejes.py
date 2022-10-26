#cordenadas X y Y
import numpy as np

m1 = np.array([[1,1],[1,1]])
m2 = np.array([[8,8],[8,8]])

print(m1)
print("")
print(m2)
print("")
#print(np.sum(m1,axis=1))
print(np.concatenate([m1,m2], axis = 1))

