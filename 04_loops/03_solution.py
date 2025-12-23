# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter number: "))

for i in range(1, 11):
    if i == 5:
        continue  # we cannot use "pass" here - as use only to pass empty conditionals
    
    print(f"{num} * {i} = {num*i}")
    