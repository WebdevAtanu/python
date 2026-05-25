try:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid number for age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")

