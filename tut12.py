'''
Python Functions
A function is a block of code that performs a specific task whenever it is called. 
In bigger programs, where we have large amounts of code, 
it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

Built-in functions
User-defined functions

Built-in functions:
These functions are defined and pre-coded in python. 
Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs. 
Such functions are called user-defined functions.
'''

def multiplication(a, b):
  return a * b

print("The value of multiplication: ",multiplication(2, 3))

def division(a, b):
  return a / b

print("The value of division: ",division(2, 3))

def power(a, b):
  return a * b

print("The value of power: ",power(2, 3))

def withoutArgs():
  print("This is a function without arguments")
  return 10*20

print("The value of without arguments" , withoutArgs())

def illMakeHimLater(a, b):
  pass # with this character i define ill Make Him Later