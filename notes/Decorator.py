# Decorators are a feature in Python that allow you to modify the behavior of a function without changing its code. They are often used for logging, access control, and other cross-cutting concerns.
def decorator(func): 
    def wrapper():                  # the wrapper function that will modify the behavior of the original function
        print("Before function")    # code to execute before the original function
        func()
        print("After function")     # code to execute after the original function
    return wrapper

@decorator                          # this is the syntax for applying a decorator to a function
def hello():
    print("Hello World")

hello()                             # when we call hello(), it will execute the wrapper function defined in the decorator, which will print "Before function", then call the original hello() function, and finally print "After function".