import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        """Calculate distance between two points"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


# Main program
x1, y1 = map(float, input("Enter coordinates of first point (x y): ").split())
x2, y2 = map(float, input("Enter coordinates of second point (x y): ").split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print("\nFirst Point:", p1)
print("Second Point:", p2)
print("Distance between points:", p1.distance(p2))

