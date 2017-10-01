import logging
import string as s
from itertools import product, count
from timeit import default_timer as timer

logging.basicConfig(
    level=logging.INFO,
    filename='brute_single.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def crack():
    """Goes through all possible character combinations until the password has been found"""

    logging.info('Beginning cracking process...')
    start = timer()

    counter = 1
    for i in count(1, 1):

        # Uses product() to produce all possible combinations of letters and numbers
        # EG: product('ab'. repeat=2)
        # --> AA, AB, BA, BB
        variations = product(letters, repeat=counter)
        for variation in variations:
            attempt = ''.join(variation)
            if attempt == password:
                end = timer()
                time = end - start
                print(f"Password is: '{attempt}'")
                print("Success in {:.2f} second(s)!".format(time))
                logging.info(f"Password is: '{attempt}'")
                logging.info('Success in {:.2f} second(s)!'.format(time))
                return

        # Increments length of string to check all combinations of by 1
        counter += 1

    # If this line is reached, password has not been found.
    # This should be impossible.
    print("Password not found.")


if __name__ == '__main__':
    # Assign correct password here.
    # crack() will compare to this variable
    password = "p4ss"
    letters = [i for i in s.ascii_letters] + [str(i) for i in range(10)]
    crack()
