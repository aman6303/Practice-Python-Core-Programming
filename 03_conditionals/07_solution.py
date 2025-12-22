size = input("Enter your coffee size: ").lower()
option = input("Extra shot true or false: ").capitalize() #captilize first word

if option:
    coffee = size  + " Coffee with extra shot"
else:
    coffee = size + " Coffee"
    
print(coffee)