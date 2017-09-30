import logging

logging.basicConfig(
    level=logging.INFO,
    filename='factorial.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def fact(num):
    logging.info("Calculating factorial of: {} ...".format(num))
    prd = 1
    numbers = [i for i in range(1, abs(int(num)) + 1)]
    for i in numbers:
        prd = prd * i
    if len(str(prd)) < 10:
        logging.info("Factorial is: {:,}".format(prd))
    else:
        logging.info("Factorial is too long to display: ({} characters)".format(len(str(prd))))
    return prd


number = input("Enter number to calculate factorial:\n")

factorial = fact(number)
print("The factorial is:\n{:,}".format(factorial))
