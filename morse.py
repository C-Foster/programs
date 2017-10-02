import logging
import string

logging.basicConfig(
    level=logging.INFO,
    filename='morse.log',
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def convert_to(a_string):
    """Returns the morse code equivalent of argument 'a_string'

    >>> convert_to('HELLO')
    '.... . .-.. .-.. --- '
    >>> convert_to('DOVAHKIIN')
    '-.. --- ...- .- .... -.- .. .. -. '
    >>> convert_to('HELLO THERE')
    '.... . .-.. .-.. --- | - .... . .-. . '
    """

    try:
        # removes punctuation from the string
        for char in string.punctuation:
            a_string = a_string.replace(char, '')

        # list of letters in original input
        string_list = [letter for letter in a_string]

        for i in range(len(string_list)):
            # remove un-convertable strings
            if string_list[i] not in morse_dict:
                del (string_list[i])

            # converts to morse code
            string_list[i] = morse_dict[string_list[i]] + " "

        # contents of 'string_list' form a string to be returned
        converted = ''.join(string_list)
        return converted
    except KeyError as e:
        print("Dictionary error:", e, "in Morse.convert_to()")
    except IndexError as e:
        print("Index error:", e, "in Morse.convert_to()")
    except Exception as e:
        print("Unknown error:", e, "in Morse.convert_to()")


def convert_from(a_string):
    """Returns the English equivalent of argument 'a_string'

    Doctests:
    >>> convert_from(".... . .-.. .-.. ---")
    'HELLO'
    >>> convert_from("-.. --- ...- .- .... -.- .. .. -.")
    'DOVAHKIIN'
    >>> convert_from(".... . .-.. .-.. --- | - .... . .-. .")
    'HELLO THERE'
    """

    try:
        string_list = []
        morse_char = ""

        # since morse code has several characters per letter, must iterate through the string
        # characters are added to 'morse_char' accordingly, then each letter equivalent is added
        for letter in a_string:
            if letter == " " or letter == "" or letter == "\n":
                string_list.append(morse_char)
                morse_char = ""
                continue
            morse_char += letter
        # ensures final characters are added to the list
        string_list.append(morse_char)

        # removes un-convertable characters
        for i in range(len(string_list)):
            if string_list[i] not in alpha_dict:
                del (string_list[i])

            # converts contents of 'string_list' to English
            if string_list[i] != " ":
                string_list[i] = alpha_dict[string_list[i]]

        # contents of 'string_list' form a string to be returned
        converted = ''.join(string_list)
        return converted
    except KeyError as e:
        print("Dictionary error:", e, "in Morse.convert_from()")
    except IndexError as e:
        print("Index error:", e, "in Morse.convert_from()")
    except Exception as e:
        print("Unknown error:", e, "in Morse.convert_from()")


# create list of all uppercase letters and a space
alpha_list = [i for i in string.ascii_uppercase] + [" "]

# create list of all morse code characters, alphabetical order
# space == |
morse_list = [".-",
              "-...",
              "-.-.",
              "-..",
              ".",
              "..-.",
              "--.",
              "....",
              "..",
              ".---",
              "-.-",
              ".-..",
              "--",
              "-.",
              "---",
              ".--.",
              "--.-",
              ".-.",
              "...",
              "-",
              "..-",
              "...-",
              ".--",
              "-..-",
              "-.--",
              "--..",
              "|"]

# create dictionaries mapping alphabet characters to morse code and vice versa
alpha_dict, morse_dict = dict(zip(morse_list, alpha_list)), dict(zip(alpha_list, morse_list))

if __name__ == '__main__':
    import doctest
    result = doctest.testmod()
    logging.info(result)
    print(result)

