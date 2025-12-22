#  Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_type = input("Enter your pet type: ").lower()
pet_age = int(input("Enter the age of the pet: "))

if  pet_type == "dog" and pet_age<2:
    print("Puppy food")
elif pet_type == "dog" and pet_age>=2:
    print("Normal dog food")
elif pet_type == "cat" and pet_age>5:
    print("Senior cat food")
elif pet_type == "cat" and pet_age<=5:
    print("Normal cat food")
else:
    print("Invalid Input")