def swap_first_n(str1, str2, n):
    """Swap the first n characters of two strings"""
    if n > len(str1) or n > len(str2):
        print("Error: n is larger than one of the strings!")
        return str1, str2

    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    return new_str1, new_str2


# Main program
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter number of characters to swap: "))

result1, result2 = swap_first_n(s1, s2, n)

print("After swapping:")
print("String 1:", result1)
print("String 2:", result2)
