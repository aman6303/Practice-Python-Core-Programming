# Problem: Write a function that takes variable number of arguments and returns their sum.

def func(*args):
    print(*args)        # Output: 2 3 4 4
    #print(type(*args))  # Output: TypeError (Unpacks args into multiple separate arguments)
    
    print(args)         # Output: (2, 3, 4, 4)
    print(type(args))   # Output: <class 'tuple'>
    
    return sum(args)  # sum is a keyword

print(func(2, 3, 4))
print(func(2, 3, 4, 4, 5, 6))