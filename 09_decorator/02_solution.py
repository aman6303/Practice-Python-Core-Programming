# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args, **kwargs)


    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Aman", "hello") # calling: greet with args aman, hello and kwargs
greet("Singh", greeting = "namaste") # calling: greet with args Singh and kwargs greeting=namaste