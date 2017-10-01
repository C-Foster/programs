import logging
import string as s

logging.basicConfig(
    level=logging.INFO,
    filename='cipher_log.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def main():
    """The main code"""

    user_input = ''
    while user_input != 'STOP':
        user_input = input("Enter the string to cipher:\n(Enter 'STOP' to exit)\n")
        logging.info(f'User entered: "{user_input}"')
        user_input = user_input.upper().strip(' ')

        # stop execution
        if user_input == 'STOP':
            return
        else:
            # remove punctuation
            for i in s.punctuation:
                user_input = user_input.replace(i, '')

            logging.info(f'Formatted input: "{user_input}"')
            output = cipher(user_input)
            print(output)
            logging.info(f'Output string: "{output}"')


def cipher(string):
    """Ciphers a string passed as an argument. Returns the ciphered string

    Doctests:
    >>> cipher('HELLO')
    'SVOOL'
    >>> cipher('DOVAHKIIN')
    'WLEZSPRRM'
    >>> cipher('0123456789')
    '9876543210'
    """

    try:
        letters = [letter for letter in string]
        for i in range(len(letters)):
            letters[i] = cipher_dict[letters[i]]
        converted = ''.join(letters)
        return converted
    except KeyError as oops:
        print(f"Dictionary error: {oops} while converting.")
    except Exception as oops:
        print(f"Unknown error: {oops} while converting.")


upper_string = [i for i in s.ascii_uppercase]  # all uppercase letters, in order
numbers = [str(i) for i in range(10)]  # 0 through 9 as strings

# create list of characters forwards
first_string = upper_string
first_string.extend(numbers)

# create list of characters in reverse
second_string = upper_string[:-10]
second_string.reverse()
second_string.extend(reversed(numbers))

# ensure both lists contain a space
first_string.append(" ")
second_string.append(" ")

# reset contents of upper_string to contain only letters
upper_string = upper_string[:-11]

# map each character to corresponding character in the reversed list
cipher_dict = dict(zip(first_string, second_string))

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
