def greet(name):
    return f"Hello {name}"

print(greet("Python"))

# default parameter
def add(a, b=10):
    return a + b

print(add(5))

# lambda function
square = lambda x: x * x
print(square(5))

# list comprehension
squares = [x*x for x in range(5)]
print(squares)

# map, filter, reduce
nums = [1, 2, 3, 4]

print(list(map(lambda x: x*2, nums)))
print(list(filter(lambda x: x%2==0, nums)))

from functools import reduce
print(reduce(lambda x, y: x+y, nums))