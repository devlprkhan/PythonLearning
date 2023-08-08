'''
Exceptions in Python

Python has many built-in exceptions that are raised 
when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops 
the current process and passes it to the calling process until it is handled. 
If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. 
The code in try block runs when there is no error. 
If the try block catches the error, then the except block is executed.
'''
# General Error Handler for All to avoid code blocking
try:
  a=int(input("Enter a number: "))
except Exception as e:
  print("Invalid input: ", e)
  
try:
  a=int(input("Enter a number: "))
except Exception as e:
  print("Invalid input: ", e)
  
# Handle specific error
try:
  a=int(input("Enter data: "))
except ValueError:
  print("Number is not a integer!")

# Handling Multiple Errors
g = [1,2,3,4]
try:
  a=int(input("Enter data: "))
  print(g[a])
except ValueError:
  print("Number is not a integer!")
except IndexError:
  print("This is not valid a index!")
  
'''
Finally Clause

The finally code block is also a part of exception handling. 
When we handle exception using the try and except block, we can include a finally block at the end. 
The finally block is always executed, so it is generally used for doing the 
concluding tasks like closing file resources or closing database 
connection or may be ending the program execution with a delightful message.
'''
def func1():
  try:
    gg=int(input("Enter data: "))
    return 1
  except:
    print("Invalid Input!")
    return 0
  finally:
    print("I'm always execute even if there is return above me")
    # I'm always execute even if there is return above me
xx = func1()
print("xx:  ", xx)