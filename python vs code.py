import cmath  # for complex numbers (if discriminant < 0)

def find_roots(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)
    
    return root1, root2

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Call the function and display the roots
root1, root2 = find_roots(a, b, c)
print(f"The roots of the quadratic equation are: {root1} and {root2}")
