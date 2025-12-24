# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    print(type(kwargs))      
    print(kwargs)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name="aman", age= 10)
print()
print_kwargs(age= 10, name="aman")
print()
print_kwargs(age= 10, name="aman", address = "Ludhiana")

# Output

# <class 'dict'>
# {'name': 'aman', 'age': 10}
# name: aman
# age: 10

# <class 'dict'>
# {'age': 10, 'name': 'aman'}
# age: 10
# name: aman

# <class 'dict'>
# {'age': 10, 'name': 'aman', 'address': 'Ludhiana'}
# age: 10
# name: aman
# address: Ludhiana