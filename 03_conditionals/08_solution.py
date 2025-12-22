pswd = input("Enter your password: ")

length_of_pswd = len(pswd)

if length_of_pswd > 10:
    strength = "Strong"
elif length_of_pswd > 6:
    strength = "Medium"
else:
    strength = "Weak"
    
print(strength)