import math     # import math module
import random   # import random module
import datetime # import datetime module
import os       # import os module
import sys      # import sys module

# ================================== math module examples ==================================
print(math.sqrt(16))            # prints the square root of 16
print(math.factorial(5))        # prints the factorial of 5
print(math.pi)                  # prints the value of pi
print(math.e)                   # prints the value of e
print(math.sin(math.pi/2))      # prints the sine of pi/2
print(math.cos(0))              # prints the cosine of 0
print(math.tan(math.pi/4))      # prints the tangent of pi/4
print(math.log(10))             # prints the natural logarithm of 10
print(math.pow(2, 3))           # prints 2 raised to the power of 3
print(math.floor(3.7))          # prints the floor of 3.7
print(math.ceil(3.7))           # prints the ceiling of 3.7
print(math.gcd(12, 18))         # prints the greatest common divisor of 12 and 18
print(math.lcm(12, 18))         # prints the least common multiple of 12 and 18
print(math.comb(5, 2))          # prints the number of combinations of 5 things taken 2 at a time
print(math.perm(5, 2))          # prints the number of permutations of 5 things taken 2 at a time
print(math.factorial(5))        # prints the factorial of 5
print(math.log10(1000))         # prints the base 10 logarithm of 1000
print(math.log2(1024))          # prints the base 2 logarithm of 1024
print(math.degrees(math.pi/2))  # prints the degrees equivalent of pi/2 radians
print(math.radians(90))         # prints the radians equivalent of 90 degrees

# ================================== random module examples ==================================
print(random.randint(1, 10))                # prints a random number between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))       # prints a random element from the list
print(random.sample([1, 2, 3, 4, 5], 3))    # prints 3 random elements from the list
print(random.random())                      # prints a random number between 0 and 1
print(random.uniform(1, 10))                # prints a random number between 1 and 10
print(random.normalvariate(0, 1))           # prints a random number from a normal distribution with mean 0 and standard deviation 1

# ================================== datetime module examples ==================================
print(datetime.datetime.now())          # prints the current date and time
print(datetime.date.today())            # prints the current date
print(datetime.datetime(2020, 1, 1))    # prints the date and time for January 1, 2020
print(datetime.timedelta(days=7))       # prints a time delta of 7 days
print(datetime.datetime.now() + datetime.timedelta(days=7)) # prints the date and time 7 days from now
print(datetime.datetime.now() - datetime.timedelta(days=7)) # prints the date and time 7 days ago
print(datetime.datetime.now().strftime("%Y-%m-%d"))         # prints the current date in the format YYYY-MM-DD
print(datetime.datetime.now().strftime("%H:%M:%S"))         # prints the current time in the format HH:MM:SS
print(datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")) # parses a date string and prints the corresponding datetime object
print(datetime.datetime.strptime("2020-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")) # parses a date and time string and prints the corresponding datetime object

# ================================== os module examples ==================================
print(os.getcwd())              # prints the current working directory
print(os.listdir())             # prints a list of files and directories in the current working directory
print(os.path.join("folder", "file.txt"))   # prints the path to a file in a subfolder
print(os.path.exists("file.txt"))           # prints True if the file exists, False otherwise
print(os.path.isfile("file.txt"))           # prints True if the path points to a file, False otherwise
print(os.path.isdir("folder"))              # prints True if the path points to a directory, False otherwise

# ================================== sys module examples ==================================
print(sys.argv)     # prints the command-line arguments passed to the script
print(sys.platform) # prints the platform information
print(sys.version)  # prints the Python version information