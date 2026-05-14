age = input("Enter your age: ") # get age from user input
age = int(age)                  # convert string to integer

if age < 18:                    # if age is less than 18
    print("Minor")
elif age == 18:                 # if age is 18
    print("Just Adult")
else:
    print("Adult")