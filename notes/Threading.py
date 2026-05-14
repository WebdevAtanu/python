import threading # Import the threading module to work with threads

# Define a function that will be run in a separate thread
def print_numbers():
    for i in range(3):
        print(i)

# Define another function that will be run in a separate thread
def print_names():
    for name in ["Alice", "Bob", "Charlie"]:
        print(name)

# Create a thread that will execute the print_numbers function
t = threading.Thread(target=print_numbers)  # Create a Thread object and specify the target function to run
n = threading.Thread(target=print_names)    # Create another Thread object for the print_names function
t.start()                                   # Start the thread, which will execute the print_numbers function in parallel with the main thread
n.start()                                   # Start the thread, which will execute the print_names function in parallel with the main thread
t.join()                                    # Wait for the thread to finish before continuing with the main thread
n.join()                                    # Wait for the thread to finish before continuing with the main thread
print("Thread has finished execution")      # Print a message after the thread has completed its task