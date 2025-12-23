# chekcing a number is prime or not

num = int(input("Enter your number: "))

# for i in range(2, num):
#     if (num% i) == 0:     #always specifiy order in paranthesis
#         print(f"Number is divisible by {i}! So it is not prime")
#         break
# else:
#     print("Number is Prime")

# we can also do it by assuming num is prime

is_prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

print(is_prime)