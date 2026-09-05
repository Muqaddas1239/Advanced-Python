#OS Module in Python

#The OS module is a built-in Python module used to interact 
# with the operating system and manage files, folders, and paths.

import os

#1. os.getcwd()

#os.getcwd() returns the location of the current working directory.

current_folder = os.getcwd()

print("Current working directory:", current_folder)

#2. os.listdir()

#os.listdir() returns the names of files and folders
#inside the current working directory.

items = os.listdir()

print("Files and folders:")

for item in items:
    print(item)

# 3. os.chdir()

# os.chdir() changes the current working directory.

#The folder must already exist.

new_folder = os.path.join(os.getcwd(), "Practice")

if os.path.exists(new_folder):
    os.chdir(new_folder)
    print("Changed directory to:", os.getcwd())
else:
    print("Practice folder does not exist.")

#4. os.mkdir()

#os.mkdir() creates a new folder.

folder = "NewFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("NewFolder created.")
else:
    print("NewFolder already exists.")

#5. os.makedirs()

#os.makedirs() creates a folder and its subfolders.

folder_path = "MainFolder/SubFolder"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("MainFolder and SubFolder created.")
else:
    print("Folders already exist.")

# 6. os.rmdir()

#os.rmdir() removes an empty folder.

folder = "NewFolder"

if os.path.exists(folder):
    os.rmdir(folder)
    print("NewFolder removed.")
else:
    print("NewFolder does not exist.")

#7. os.remove()

#os.remove() deletes a file.

file_name = "example.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted.")
else:
    print("example.txt does not exist.")

#8. os.rename()

#os.rename() changes the name of a file or folder.

old_name = "old.txt"
new_name = "new.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed.")
else:
    print("old.txt does not exist.")

#9. os.path.exists()

# os.path.exists() checks whether a file or folder exists.

path = "MainFolder"

if os.path.exists(path):
    print("The path exists.")
else:
    print("The path does not exist.")

#10. os.path.join()

#os.path.join() joins different parts of a path.

folder = "MainFolder"
file = "data.txt"

path = os.path.join(folder, file)

print("Complete path:", path)