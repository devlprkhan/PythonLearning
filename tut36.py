'''
seek() and tell() functions

In Python, the seek() and tell() functions are used to 
work with file objects and their positions within a file. 
These functions are part of the built-in io module, 
which provides a consistent interface for reading and writing to various
file-like objects, such as files, pipes, and in-memory buffers.
'''

with open('file.txt') as f:
  f.seek(12) # Move to the 12th byte in the file
  
  # Save the current position
  current_position = f.tell()
  print(current_position) #12
  
  # Read the next 6 bytes
  print(f.read())
  
'''
truncate() function

When you open a file in Python using the open function, 
you can specify the mode in which you want to open the file. 
If you specify the mode as 'w' or 'a', the file is
opened in write mode and you can write to the file. 
However, if you want to truncate the file to a specific size, 
you can use the truncate function.
'''

with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5) #Hello (truncate to only 5 characters)