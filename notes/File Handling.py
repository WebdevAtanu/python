data = open("test.txt");    # open file in read mode
print(data.read())          # read content of file
data.close()                # close file

# write
# with open("test.txt", "w") as f: # "r" = read, "w" = write
#     f.write("This is a text file") # write to file

# read
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)

