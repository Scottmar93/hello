import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

print("hello world")

print("now add a different line")

print("This is a new line to add")

print("now we have both lines")

print("I am now checking out this second branch and making changes")

plt.plot(x, y)
plt.title("Sine")
plt.xlabel("x")
plt.show()
