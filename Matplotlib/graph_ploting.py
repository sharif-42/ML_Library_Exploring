"""
https://towardsdatascience.com/introduction-to-matplotlib-in-python-5f5a9919991f
"""

import matplotlib.pyplot as plt

# Draw Line Graph
x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
squares_ = [10, 15, 14, 19, 17, 25, 36, 49, 74]

plt.plot(x_values, squares)
plt.title = "Line Drawing"
plt.show()

# Bar graphs
plt.bar(x_values, squares, color="green")
plt.show()

# Bar Graph Horizontal
plt.barh(x_values, squares, color="green")
plt.show()

# Scatter Plots
plt.scatter(x_values, squares, s=30, color="red")
plt.scatter(x_values, squares_, s=30, marker='*', color="green")
plt.show()

# Histogram
plt.hist(squares_, bins=15, color='blue', alpha=0.5)
plt.show()
