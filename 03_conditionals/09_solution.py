year = int(input("Enter year value: "))

if year%100 == 0:
    if year%400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
        
elif year%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")