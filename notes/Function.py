def greet(name):
    return f"Hello {name}"  # f-string is used to concatenate string

print(greet("Python"))      # Hello Python

# default parameter
def add(a, b=10):
    return a + b

result = add(5, 10)         # function call
print(result)

# lambda function
square = lambda x: x * x    # anonymous function, can be used where function is required as argument
print(square(5))

# list comprehension
squares = [x*x for x in range(5)] # creates a list of squares from 0 to 4
print(squares)

# map, filter, reduce
nums = [1, 2, 3, 4] 
print(list(map(lambda x: x*2, nums)))
print(list(filter(lambda x: x%2==0, nums)))

# reduce is used to apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.
from functools import reduce 
print(reduce(lambda x, y: x+y, nums)) # 10