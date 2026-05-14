# Exception handling is a mechanism to handle errors gracefully in Python. It allows you to write code that can handle exceptions without crashing the program. The main keywords used in exception handling are try, except, else, and finally.
try:
    x = 10 / 0              # this will raise a ZeroDivisionError
except ZeroDivisionError:   # this block will execute if a ZeroDivisionError is raised
    print("Cannot divide by zero")
finally:
    print("Always runs")

try:
    x = int("abc")          # this will raise a ValueError
except ValueError:          # this block will execute if a ValueError is raised
    print("Invalid input")
else:                       # this block will execute if no exception is raised
    print("Conversion successful")
finally:                    # this block will always execute
    print("End of program")