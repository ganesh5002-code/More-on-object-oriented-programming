class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
value_radius = float(input("Enter the radius of the circle: "))
the_circle = Circle(value_radius)

print("The area of the circle is:", the_circle.area())
print("The perimeter of the circle is:", the_circle.perimeter())



