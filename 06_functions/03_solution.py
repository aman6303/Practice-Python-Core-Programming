# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(input1, input2):
    return input1*input2        # * already suppot function overloading(polymorphism)

result = multiply(10,2)
result2 = multiply("aman",3)

print(result)
print(result2)

