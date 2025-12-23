# Problem: Given a string, find the first non-repeated character.

str = input("Enter your string: ")

# visited_char = ""
# repeated_char = ""

# for char in str:
#     if char not in visited_char:
#         visited_char += char
#     else:
#         repeated_char += char

# for i in visited_char:
#     if i not in repeated_char:
#         print(i)
#         break
# else:
#     print("all char are repeating")
        
# we can solve the same problem using str.count(char) method which returns no of times char repeating in str

for char in str:
    if str.count(char) == 1:
        print(char)
        break
else:
    print("all value are repeating") # this line will only execute if loop is not terminated by break