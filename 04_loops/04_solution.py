# Problem: Reverse a string using a loop.

str = input("Enter your string: ")

rev_str = ""  #empty string

for char in str:
    rev_str = char + rev_str
    
print(rev_str)