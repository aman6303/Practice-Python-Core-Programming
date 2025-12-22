
fruit = "Banana"

fruit_color = input("Enter the color of fruit: ")

if fruit_color not in ["Green", "green", "Yellow", "yellow", "Brown", "brown"]:
    exit()
    
if fruit=="Banana":
    if fruit_color=="Green" or fruit_color=="green":
        print("Unripe")
        
    if fruit_color=="Yellow" or fruit_color=="yellow":
        print("Ripe")
        
    if fruit_color=="Brown" or fruit_color=="brown":
        print("Overripe")