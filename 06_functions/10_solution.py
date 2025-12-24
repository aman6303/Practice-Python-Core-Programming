# Problem: Create a recursive function to calculate the factorial of a number.

def fact(num):
    if num == 1:               # we need to think of exit strategy in recursion
        return 1               # we do not to need write else as after return rest part of code doesnt run
    return num * fact(num-1)
    
result = fact(6)
print(result)