# Experiment No. 10
# Program to plot different graphs using Matplotlib

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 3. Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 4. Box Plot
plt.figure()
plt.boxplot(y)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()