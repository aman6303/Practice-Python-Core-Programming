# Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter the value of N: "))

even_num_sum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        even_num_sum += i

print(even_num_sum)