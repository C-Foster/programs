fibonacci = {}


def fib(n):
    value = None
    if n in fibonacci:
        return fibonacci[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)

    fibonacci[n] = value
    return value


if __name__ == '__main__':
    for i in range(1, 101):
        print('{}: {:,}'.format(i, fib(i)))