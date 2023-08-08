'''
OS Module in Python

The os module in Python is a built-in library that provides 
functions for interacting with the operating system. 
It allows you to perform a wide variety of tasks, 
such as reading and writing files, interacting with the file system, 
and running system commands.

Here are some common tasks you can perform with the os module:
'''
import os

#* Generate Folders
# If Exists don't create
if (not os.path.exists("osModule/Generate Folders")):
  os.mkdir("osModule/Generate Folders")
  # Generate Sub folders as well
  for i in range(0, 10):
    os.mkdir(f"osModule/Generate Folders/Sub-Generated-Folder {i+1}")
    
#* Read Files
# Open the file in read-only mode
file = os.open("osModule/readme.md", os.O_RDONLY)
# Read the contents of the file
content = os.read(file, 1024)
print("File content: ", content)
# Close the file
os.close(file)

#* Write Files
file2 = os.open("osModule/readme.md", os.O_WRONLY)
# Write to the file
os.write(file2,b"This is from Python Code, Hello, world!")
# Close the file
os.close(file2)

#* Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['.vscode', 'Fun PR', 'haseeb.py', ...]

#* Run the "ls" command and print the output
output = os.getcwd()
print(output)