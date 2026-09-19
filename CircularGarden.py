import math
Radius = int(input("Enter the radius of the circle in meters: "))

Area = math.pi * Radius**2
Circumference = 2 * math.pi * Radius
square_root = math.sqrt(Area)
rounded_up = math.floor(Area)
rounded_down = math.ceil(Area)
print("The area is : ", Area)
print("The circumference is : ", Circumference)
print("The square root is : ", square_root)
print("The rounded up area is : ", rounded_up)
print("The rounded down area is : ", rounded_down)