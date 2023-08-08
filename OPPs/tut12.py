'''
dir(), __dict__ and help() methods in python

We must look into dir(), __dict__() and help() attribute/methods in python. 
They make it easy for us to understand how classes resolve various functions 
and executes code. In Python, there are three built-in functions that are 
commonly used to get information about objects: dir(), dict, and help(). 
Let's take a look at each of them:
'''

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)

#? dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
print(dir(Person))
#? __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes.
#* return passed parameters as a dictionary
print(p.__dict__) #{'name': 'John', 'age': 30, 'version': 1}
#? help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods
print(help(Person))