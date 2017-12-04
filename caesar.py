from string import ascii_lowercase as letters


def encrypt(message, shift):
    msg = message.lower()
    encrypted_msg = ''

    for letter in msg:
        if letter in letters:
            num = ord(letter)
            num += shift
            
            if num > ord("z"):
                num -= 26
                
            char = chr(num)
            encrypted_msg += char
        else:
            encrypted_msg += letter

    return encrypted_msg


def decrypt(message):
    msg = message.lower()
    decrypted_list = []

    for x in range(26):
        encrypted_msg = ''
        for letter in msg:
            if letter in letters:
                num = ord(letter)
                num -= x
                
                if num < ord("a"):
                    num += 26
                    
                char = chr(num)
                encrypted_msg += char
            else:
                encrypted_msg += letter
        decrypted_list.append("{} = {}".format(encrypted_msg, x))

    return decrypted_list     


def main():
    try:
        usr_shift = int(input("Enter the shift: "))
    except:
        return

    usr_msg = input("Enter your message: ")
    encrypted = encrypt(usr_msg, usr_shift)
    print("The encrypted message is:\n")
    print(encrypted)


if __name__ == "__main__":
    usr_input = ''
    while usr_input != "EX":
        usr_input = input("Enter 'EX' to end.").upper()
        if usr_input == "EX":
            break
        else:
            main()

    usr_encrypted = input("Enter a message to decrypt: ")
    decrypted_messages = decrypt(usr_encrypted)

    for i in decrypted_messages:
        print(i)
