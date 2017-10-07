import logging
from cmath import sqrt as complex_root
from math import sqrt as root

logging.basicConfig(
    level=logging.INFO,
    filename='quadratics.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def main():
    var_a = input("Enter the value of A:\n")
    var_b = input("Enter the value of B:\n")
    var_c = input("Enter the value of C:\n")
    my_vars = (var_a, var_b, var_c)

    # stops execution of the program if any inputs are left blank
    for var in my_vars:
        if var == "":
            return

    if not verify(var_a, var_b, var_c):
        print("Invalid input.\n")
        main()
    else:
        print(f"\nValues: A = {var_a}, B = {var_b}, C = {var_c}\n")
        output = calc(var_a, var_b, var_c)
        logging.info(f'Numbers entered: A: {var_a}, B: {var_b}, C: {var_c}')
        logging.info(output)
        print(output)


def verify(var1, var2, var3):
    """Checks for valid inputs

    >>> verify(1, 6, 8)
    True
    >>> verify(2, 5, 0)
    False
    """

    var1, var2, var3 = str(var1), str(var2), str(var3)
    check_vars = [var1, var2, var3]
    for var in check_vars:
        if var.isalpha() or var == '0':
            verification_result = False
            break
    else:
        verification_result = True
    return verification_result


def calc(a, b, c):
    """Returns the roots of a quadratic equation of the form 'Ax^2 + Bx + C' (if any)
    Can handle complex roots

    Doctests:
    >>> calc(1, 6, 8)
    'x = -2.0, x = -4.0'
    >>> calc(1, -6, 8)
    'x = 4.0, x = 2.0'
    >>> calc(-4, 12, -9)
    'x = 1.5'
    >>> calc(2, 5, 10)
    'x = (-1.25+1.8540496217739157j), x = (-1.25-1.8540496217739157j)'
    """

    try:
        a, b, c = float(a), float(b), float(c)
        discriminant = b * b - 4 * a * c
        divisor = a * 2

        # if the value of the discriminant is more than zero, the equation has real roots
        if discriminant > 0:
            result_plus = (-b + (root(discriminant))) / divisor
            result_minus = (-b - (root(discriminant))) / divisor
            output = f'x = {result_plus}, x = {result_minus}'
            return output

        # if the value of the discriminant is equal to zero, the equation has one real root
        elif discriminant == 0:
            calc_result = (-b + (root(discriminant))) / divisor
            output = f'x = {calc_result}'
            return output

        # if the value of the discriminant is less than zero, the equation has no real roots
        elif discriminant < 0:
            result_plus = (-b + (complex_root(discriminant))) / divisor
            result_minus = (-b - (complex_root(discriminant))) / divisor
            output = f'x = {result_plus}, x = {result_minus}'
            return output

    except ValueError as e:
        logging.info(f"Calculation error: {e} during calculation.")
        print(f"Calculation error: {e} during calculation.")
    except Exception as e:
        logging.info(f"Unknown error: {e} during calculation.")
        print(f"Unknown error: {e} during calculation.")


if __name__ == '__main__':
    choice = ''
    while choice != 'stop':
        choice = input('Do you want to run stop?').lower()
        if choice == 'run':
            main()
        # test mode: runs doctests
        elif choice == '--test':
            import doctest
            result = doctest.testmod()
            logging.info(f'Running test.\n{result}')
        elif choice == 'stop':
            break
