import matplotlib.pyplot as plt
import numpy as np

values = np.array([0.1,0.5])
labels = ["value 1", "value 2"]
plt.pie(values , labels = labels ,  radius= 2)
plt.show()