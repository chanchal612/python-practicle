def process_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    # a) Count characters, words, lines
    num_lines = len(lines)
    num_chars = sum(len(line) for line in lines)
    num_words = sum(len(line.split()) for line in lines)

    print(f"Total characters: {num_chars}")
    print(f"Total words: {num_words}")
    print(f"Total lines: {num_lines}")

    # b) Character frequency using dictionary
    char_freq = {}
    for line in lines:
        for ch in line:
            char_freq[ch] = char_freq.get(ch, 0) + 1

    print("\nCharacter Frequencies:")
    for ch, freq in char_freq.items():
        print(repr(ch), ":", freq)

    # c) Print words in reverse order
    all_words = []
    for line in lines:
        all_words.extend(line.split())
    print("\nWords in reverse order:")
    print(" ".join(all_words[::-1]))

    # d) Copy even and odd lines to different files
    with open("File1.txt", "w") as f1, open("File2.txt", "w") as f2:
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:   # even line
                f1.write(line)
            else:            # odd line
                f2.write(line)

    print("\nEven lines copied to File1.txt")
    print("Odd lines copied to File2.txt")


# Main program
filename = input("Enter filename: ")
process_file(filename)
