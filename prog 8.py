# Take input from user
data = input("Enter elements of the list separated by spaces: ").split()

# Convert numeric inputs to int/float, keep others as string
processed_list = []
for item in data:
    if item.isdigit():             # integer
        processed_list.append(int(item))
    else:
        try:
            processed_list.append(float(item))   # check if float
        except ValueError:
            processed_list.append(item)          # keep as string

# a) Using 'for' loop
cubes_for = []
for item in processed_list:
    if isinstance(item, int) and item % 2 == 0:   # only even integers
        cubes_for.append(item ** 3)

print("Using for loop:", cubes_for)

# b) Using list comprehension
cubes_comp = [x ** 3 for x in processed_list if isinstance(x, int) and x % 2 == 0]

print("Using list comprehension:", cubes_comp)

