def char_frequency(s, ch):
    """a. Find the frequency of a character in a string"""
    return s.count(ch)


def replace_char(s, old, new):
    """b. Replace a character by another character in a string"""
    return s.replace(old, new)


def remove_first_occurrence(s, ch):
    """c. Remove the first occurrence of a character from a string"""
    index = s.find(ch)
    if index != -1:
        return s[:index] + s[index+1:]
    return s


def remove_all_occurrences(s, ch):
    """d. Remove all occurrences of a character from a string"""
    return s.replace(ch, '')


# Main program
string = input("Enter a string: ")
char = input("Enter a character to work with: ")

# a) Frequency
print(f"Frequency of '{char}' in string: {char_frequency(string, char)}")

# b) Replace
new_char = input("Enter a character to replace it with: ")
print("After replacement:", replace_char(string, char, new_char))

# c) Remove first occurrence
print("After removing first occurrence:", remove_first_occurrence(string, char))

# d) Remove all occurrences
print("After removing all occurrences:", remove_all_occurrences(string, char))
