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

# if a is positive, y-axis is drawn up to the highest value of f(x)
if a > 0:
    plt.plot([0, 0], [max(y_array), -(max(y_array))], label="y-axis")  # plots the y-axis

# if a is negative, y-axis is drawn up to the absolute value of the lowest value of f(x)
elif a < 0:
    plt.plot([0, 0], [abs(min(y_array)), min(y_array)], label="y-axis")  # plots the y-axis

# configure graph
plt.title(f"Graph of f(x) = {a}x^2 + {b}x + {c}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# display graph
plt.show()
