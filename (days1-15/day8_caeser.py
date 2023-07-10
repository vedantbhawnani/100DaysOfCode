def caeser(plain_text, shift_amount, code):
    result = ''
    if code == 'de':
        shift_amount *= -1
    for letter in range(0, len(plain_text)):
        position = plain_text[letter]
        finalPos = ord(position) + shift_amount
        result += chr(finalPos)
    print(f"The {code}coded text is: {result}.")
    repeat()


def repeat():
    choice = input("Go again? y/n: ")
    if choice == 'y':
        main()
    if choice == 'n':
        exit()


def main():
    word = input("String input: ")
    shift = int(input("Shift: "))
    crypt = input("'en'crypt or 'de'crypt: ")
    caeser(word, shift, crypt)


main()
