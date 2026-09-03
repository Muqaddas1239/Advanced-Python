#File Handling:
#File handling refers to the process of performing operations on a file 
# such as creating, opening, reading, writing and closing it through a programming interface

# mode: r-read, w- write, a-append
# open file
file=open("Test File.txt", "r")

# read a file
file=open("Test File.txt", "r")
content=file.read()   #read entire data
print(content)
file.close()   #best practice 

# to read first line

file=open("Test File.txt", "r")
content=file.readline()   #read first line
print(content)
file.close() 

# Read as list

file=open("Test File.txt", "r")
content=file.readlines()   #read lines
print(content)
file.close() 

# write to a file

file=open("Test File1.txt", "w")   # write code created a new file
file.write("Writing data through coding in my new file")
file.close()

file=open("Test File1.txt", "w")   # write code created a new file
file.write("Writing data through coding in my new file! checking overwrite")
file.close()

#
file=open("Test File1.txt", "a")      # append mode
file.write("\nYes its working")
file.close()

# close a file
# using with statement

with open("Test File1.txt", "r") as file:
    content=file.read()
    print(content)

# Checking File Properties

f = open("Test File1.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

# Handling Exceptions When Closing a File

try:
    file = open("Test File1.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()
