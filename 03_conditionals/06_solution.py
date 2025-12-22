distance = int(input("Enter the distance value: "))

if distance > 15:
    mode = "Car"
elif distance > 3:
    mode = "Bike"
elif distance > 0:
    mode = "Walk"

print(mode)