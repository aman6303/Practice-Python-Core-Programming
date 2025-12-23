# Problem: Keep asking the user for input until they enter a number between 1 and 10.


# n = int(input("Enter your number: "))

# while n<=1 or n>=10:
#     n = int(input("Enter your number again: "))


while True:
    number = int(input("Enter value between 1 and 10: "))
    
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, Try again!")