import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 5, 0.5)
y = x**4+18
print(x)
print(y)
plt.plot(x,y)
plt.show()
