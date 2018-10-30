import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

print("hello world")

plt.plot(x, y)
plt.title("Sine")
plt.xlabel("x")
plt.show()
