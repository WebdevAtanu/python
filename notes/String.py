name = "Superman" 
company ='DC Comics'
friends = '''
Batman
Robin
''' # multi line string

print(name[0]) # first character
print(name[-1]) # last character
print (name[1:4]) # second to fourth character
print (name + " " + company + " " + friends) # concatenation

split = company.split(" ") # split string
print(split)

print(len(name)) # length of string
print(name.find("er")) # index of character
print(name.replace("er", "ar")) # replace character

print(name.upper()) # uppercase
print(name.lower()) # lowercase

print(name.isupper()) # check if uppercase
print(name.islower()) # check if lowercase

print(name.startswith("Su")) # check if starts with
print(name.endswith("an")) # check if ends with

print(name.count("a")) # count character

print(name.capitalize()) # capitalize first character
print(name.title()) # capitalize first character of each word

print(name * 3) # repeat string

print("Hello\tWorld") # tab
print("Hello\nWorld") # new line

