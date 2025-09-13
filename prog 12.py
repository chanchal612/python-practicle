# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a) Print half values in one line and the other half in next line
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b) Tuple of even numbers
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers tuple:", even_tuple)

# c) Concatenate with t2
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d) Maximum and minimum
print("Maximum value:", max(t3))
print("Minimum value:", min(t3))
