import matplotlib.pyplot as plt

a = int(input("Enter coefficient of x^2:\n"))
b = int(input("Enter coefficient of x:\n"))
c = int(input("Enter constant:\n"))

x_array = list(range(-20, 21))
y_array = []

for x in x_array:
    y_array.append((a * (x ** 2)) + (b * x) + c)

plt.plot(x_array, y_array)
plt.title(f"Graph of f(x) = {a}x^2 + {b}x + {c}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()