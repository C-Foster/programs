import logging
from random import randint
from timeit import default_timer as timer

logging.basicConfig(
    level=logging.INFO,
    filename='bubble.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def main():
    """The main code of the program"""

    user_inputs = []
    for i in range(randint(1000, 9999)):
        user_inputs.append(randint(1, 999))

    start = timer()
    sorted_list = bubble_sort(user_inputs)
    end = timer()
    time = end - start

    for i in sorted_list:
        print(i)

    logging.info("List of size {:,} sorted in {:.2f} second(s)!".format(len(sorted_list), time))
    print("\nList of size {:,} sorted in {:.2f} second(s)!".format(len(sorted_list), time))


def bubble_sort(input_list):
    """Returns the sorted version of a list of numbers

    >>> bubble_sort([15, 3, 5, 7, 12.5])
    [3, 5, 7, 12.5, 15]
    >>> bubble_sort([1.75, 1.25, 1.5, 3, 10, 0.56, 0.51])
    [0.51, 0.56, 1.25, 1.5, 1.75, 3, 10]
    """

    for pass_number in range(len(input_list) - 1, 0, -1):
        for i in range(pass_number):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list


if __name__ == '__main__':
    choice = ''
    while choice != 'test' and choice != 'run':
        choice = input('Test or run?\n').lower()
    if choice == 'test':
        import doctest
        result = doctest.testmod()
        logging.info(f'Running test.\n{result}')
    elif choice == 'run':
        main()
