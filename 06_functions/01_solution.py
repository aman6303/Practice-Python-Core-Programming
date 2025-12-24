# Problem: Write a function to calculate and return the square of a number.

# def square(number):  # parameter
#     return (number * number)

# print(square(int(input("Enter your number: ")))) # argument

def square(number):  # number is parameter
    return (number**2)

result = square(4)  # 4 is argument

print(result)