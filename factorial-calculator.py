import logging

logging.basicConfig(
    level=logging.INFO,
    filename='factorial.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def fact(num):
    logging.info(f"Calculating factorial of: {num} ...")
    numbers = [i for i in range(abs(int(num)), 0, -1)]
    prd = 1
    for i in numbers:
        prd *= i

    if len(str(prd)) < 10:
        logging.info("Factorial is: {:,}".format(prd))
    else:
        logging.info("Factorial too long to display. ({} characters)".format(len(str(prd))))
    return prd


if __name__ == '__main__':
    number = int(input("Enter number to calculate factorial:\n"))
    factorial = fact(number)
    print("The factorial is:\n{:,}".format(factorial))
