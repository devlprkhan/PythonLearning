'''
Python provides several ways to manipulate files. 

Opening a File
Before we can perform any operations on a file, we must first open it. 
Python provides the open() function to open a file. It takes two arguments: 
the name of the file and the mode in which the file should be opened. 
The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:
f = open('myfile.txt', 'r')

By default, the open() function returns a file object that can be used 
to read from or write to the file, depending on the mode.

Modes in file
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
create (x): This mode creates a file and gives an error if the file already exists.
text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
binary (b): used to handle binary files (images, pdfs, etc).
'''

#* Reading from a File
f1 = open("my.txt", 'r')
text = f1.read()
print("Reading: ",text)
#* Closing a File
f1.close()
#* Writing to a File
f1 = open("my.txt", 'r+')
f1.write('Hello, world!, New Content!')
f1.close()
# Read New Content
f1 = open("my.txt", 'r+')
text = f1.read()
print("Reading: ",text)
f1.close()

#* Append in file
f1 = open("my.txt", 'a')
f1.write('Hello, world!, Append!')
f1.close()
# Read New Content
f1 = open("my.txt", 'r')
text = f1.read()
print("Reading: ",text)
f1.close()

#* The 'with' statement
with open("my.txt", 'r+') as f11: #with "with" we don't need to use the close() method
  text = f11.read()
  print("Reading: ",text)