def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)
