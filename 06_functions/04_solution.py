# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def func(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    
    return circumference, area

circumference, area = func(6)

print(round(circumference,4))
print(round(area,4))