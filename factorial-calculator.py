import doctest
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='factorial.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def calculate_factorial(num):
    """Returns the factorial of a given integer, num

    Doctests:
    >>> calculate_factorial(3)
    6
    >>> calculate_factorial(5)
    120
    >>> calculate_factorial(6)
    720
    >>> calculate_factorial(13)
    6227020800
    """

    logging.info(f"Calculating factorial of: {num} ...")
    numbers = [i for i in range(abs(int(num)), 0, -1)]
    prd = 1
    for i in numbers:
        prd *= i
    return prd


if __name__ == '__main__':
    user_input = ''
    while user_input != 'stop':
        user_input = input(
            'Enter number to calculate factorial:\n'
            '(Enter "stop" to exit)\n'
        )

        if user_input == 'stop':
            break
        elif user_input == '--test':
            result = doctest.testmod()
            logging.info(result)
        else:
            output = calculate_factorial(user_input)
            if len(str(output)) < 10:
                logging.info("Factorial is: {:,}".format(output))
            else:
                logging.info("Factorial too long to display. ({} characters)".format(len(str(output))))
            print("The factorial is:\n{:,}".format(output))