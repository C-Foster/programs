import logging
import string as s
from itertools import product, count
from timeit import default_timer as timer

logging.basicConfig(filename='brute_single.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

password = "p4ss"
letters = [i for i in s.ascii_letters] + [str(i) for i in range(10)]


def crack():
    """Goes through all possible character combinations until the password has been found"""
    logging.info('Beginning cracking process...')
    start = timer()
    counter = 1
    for iterator in count(1, 1):
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
        counter += 1
    else:
        print("Password not found.")


if __name__ == '__main__':
    crack()
