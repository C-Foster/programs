import morse

operation = ''
while operation != "to" and operation != "from":
    print("Convert TO or FROM morse-code?")
    operation = input().lower()
    if operation != "to" and operation != "from":
        print("Invalid input.")

print("Enter the string to convert:")
string = input().upper()

result = morse.convert_to(string) if operation == "to" else morse.convert_from(string)

print(result)
