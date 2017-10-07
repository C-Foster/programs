import matplotlib.pyplot as plt

# take inputs
a = int(input("Enter coefficient of x^2:\n"))
b = int(input("Enter coefficient of x:\n"))
c = int(input("Enter constant:\n"))

# generate table of values
x_array = list(range(-20, 21))
y_array = []

# populate y-values
for x in x_array:
    y_array.append((a * (x ** 2)) + (b * x) + c)

# plot data
plt.plot(x_array, y_array, label="graph")  # plots the graph of the function
plt.plot([max(x_array), min(x_array)], [0, 0], label="x-axis")  # plots the x-axis
plt.plot([0, 0], [max(y_array), min(y_array) - (max(y_array) / 2)], label="y-axis")  # plots the y-axis

# configure graph
plt.title(f"Graph of f(x) = {a}x^2 + {b}x + {c}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# display graph
plt.show()
