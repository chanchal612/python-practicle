class InvalidNameError(Exception):
    """Custom exception for invalid names"""
    pass

def validate_name(name):
    if not name.isalpha():   # allows only alphabets
        raise InvalidNameError("Name should not contain digits or special characters.")
    return True

# Main program
try:
    user_name = input("Enter your name: ")
    validate_name(user_name)
    print("Valid Name:", user_name)
except InvalidNameError as e:
    print("Error:", e)
