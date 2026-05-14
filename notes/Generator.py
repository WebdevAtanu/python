# Generator functions are defined like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example of a generator function is shown below.
def my_gen():
    yield 1 
    yield 2
    yield 3

for val in my_gen():
    print(val)

