import string


def convert_to(a_string):
    try:
        string_list = []
        for char in string.punctuation:
            a_string = a_string.replace(char, '')
        for letter in a_string:
            string_list.append(letter)
        for i in range(len(string_list)):
            if string_list[i] not in morse_dict:
                del (string_list[i])
            string_list[i] = morse_dict[string_list[i]] + " "
        converted = ''.join(string_list)
        return converted
    except KeyError as e:
        print("Dictionary error:", e, "in Morse.convert_to()")
    except IndexError as e:
        print("Index error:", e, "in Morse.convert_to()")
    except Exception as e:
        print("Unknown error:", e, "in Morse.convert_to()")


def convert_from(a_string):
    try:
        string_list = []
        morse_char = ""
        for letter in a_string:
            if letter == " " or letter == "" or letter == "\n":
                string_list.append(morse_char)
                morse_char = ""
                continue
            morse_char += letter
        string_list.append(morse_char)
        for i in range(len(string_list)):
            if string_list[i] not in alpha_dict:
                del (string_list[i])
            if string_list[i] != " ":
                string_list[i] = alpha_dict[string_list[i]]
        converted = ''.join(string_list)
        return converted
    except KeyError as e:
        print("Dictionary error:", e, "in Morse.convert_from()")
    except IndexError as e:
        print("Index error:", e, "in Morse.convert_from()")
    except Exception as e:
        print("Unknown error:", e, "in Morse.convert_from()")


alpha_list = [i for i in string.ascii_uppercase] + [" "]

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

alpha_dict, morse_dict = dict(zip(morse_list, alpha_list)), dict(zip(alpha_list, morse_list))
