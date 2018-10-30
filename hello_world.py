import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

print("hello world")

print("This is a new line to add")

plt.plot(x, y)
plt.title("Sine")
plt.xlabel("x")
plt.show()
