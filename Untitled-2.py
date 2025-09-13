def check_character(ch):
    # a) Check if it's a letter, digit, or special character
    if ch.isalpha():
        print(f"{ch} is a Letter")
        # b) Check uppercase or lowercase
        if ch.isupper():
            print("It is Uppercase.")
        else:
            print("It is Lowercase.")
    elif ch.isdigit():
        print(f"{ch} is a Numeric Digit")
        # c) Print digit name
        digit_names = {
            '0': "ZERO", '1': "ONE", '2': "TWO", '3': "THREE", '4': "FOUR",
            '5': "FIVE", '6': "SIX", '7': "SEVEN", '8': "EIGHT", '9': "NINE"
        }
        print("Digit in words:", digit_names[ch])
    else:
        print(f"{ch} is a Special Character")


# Main program
char = input("Enter a single character: ")

if len(char) == 1:
    check_character(char)
else:
    print("Please enter only one character.")
