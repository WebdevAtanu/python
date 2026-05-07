fruits = ["apple", "banana", "mango", "lemon", "litchi"] 
print(fruits)
print(fruits[1:4]) # index 1 to 3

numbers = [5, 2, 1, 8, 6] # unsorted list of numbers
numbers.sort() # sort the list
print(numbers) 
print(sorted(numbers)) # sort the list
print(sorted(numbers, reverse=True)) # sort the list in reverse
numbers.insert(2, 3) # insert 3 at index 2
numbers.remove(1) # remove 1 from the list
numbers.pop() # remove the last element from the list
numbers.append(4) # add 4 to the end of the list