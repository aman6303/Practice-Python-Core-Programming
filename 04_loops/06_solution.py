# Problem: Compute the factorial of a number using a while loop.

n = int(input("Enter your number: "))

fact = 1

while n>0:
    fact *= n
    n -= 1
    
print(fact)