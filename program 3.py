def pyramid(n):
    """Prints a pyramid of '*' of height n"""
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def reverse_pyramid(n):
    """Prints a reverse pyramid of '*' of height n"""
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


# Main program
rows = int(input("Enter number of rows: "))

print("\nPyramid:")
pyramid(rows)

print("\nReverse Pyramid:")
reverse_pyramid(rows)
