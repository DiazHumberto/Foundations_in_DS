"""
Practicing in Matplotlib
"""

from matplotlib import pyplot as plt

x_values = [1, 2, 5, 4, 4]
y_values = [5, 4, 8, 6, 9]

plt.scatter(x_values, y_values)

other_x_values = [1, 2, 6, 8, 4]
other_y_values = [8, 7, 9, 5, 5]

plt.plot(other_x_values, other_y_values, color = "navy")

plt.title("This is the title of the plot")

plt.xlabel("x values")
plt.ylabel("y values")

plt.show()
