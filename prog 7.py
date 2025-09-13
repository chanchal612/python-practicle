def find_occurrences(text, sub):
    """Return all indices of occurrences of sub in text, or -1 if not found"""
    indices = []
    start = 0
    while True:
        index = text.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1   # move one step ahead to find next occurrence
    return indices if indices else -1


# Main program
s1 = input("Enter the main string: ")
s2 = input("Enter the substring to search: ")

result = find_occurrences(s1, s2)
print("Occurrences:", result)
