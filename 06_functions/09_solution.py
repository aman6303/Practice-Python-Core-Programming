# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_generator(limit):
    # li = []
    # for i in range(2, limit+1, 2):
    #     li.append(i)
    # return(li)   ----- but we want numbers in output
    
# print(even_generator(10))

# we cannot do this
# def even_generator(limit):
#     for i in range(2, limit+1, 2):
#         return i

# for num in even_generator(10):
#     print(num)  --------> Error: Int object are not iterable     
    
    
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):  # python will internally remember which loop have called the func
    print(num)           # if the same loop will call again -- yield will start generating from same point
                          
# if the new loop will call it -- it start generating from beginning(start)

for i in even_generator(4):
    print(i)
    
# output
# 2
# 4
# 6
# 8
# 10
# 2
# 4