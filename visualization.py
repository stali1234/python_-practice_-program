import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x ** 2 + 3
print(x, y)
# reference
plt.plot(x, y, label="stock price")
plt.title("my line plot")
plt.xlabel("stalin")
plt.ylabel("rayan")
plt.legend()
plt.show()

