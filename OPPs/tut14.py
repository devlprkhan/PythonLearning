'''
Magic/Dunder Methods in Python

These are special methods that you can define in your classes, 
and when invoked, they give you a powerful way to manipulate objects and 
their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding 
their names, are powerful tools that allow you to customize the behaviour of 
your classes. They are used to implement special 
methods such as the addition, subtraction and comparison operators, 
as well as some more advanced techniques like descriptors and properties.
'''  
import random
import string

#? __init__ method The init method is a special method that is automatically invoked when you create a new instance of a class.

class Employee:
  def __init__(self, name):
    self.name = name

p1 = Employee("Haseeb Khan")
print(p1.name)

'''
__str__ and __repr__ methods

The str and repr methods are both used to convert an object to a string 
representation. The str method is used when you want to print out an object, 
while the repr method is used when you want to get a string representation 
of an object that can be used to recreate the object.
'''

class Employee:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"My Name is {self.name}! from str"
  
  def __repr__(self):
    return f"My Name is {self.name}! from repr"
  
p2 = Employee("Haseeb Khan")

print(str(p2))
print(repr(p2))

#? __len__ method The len method is used to get the length of an object.
class Employee:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"My Name is {self.name}! from str"
  
  def __repr__(self):
    return f"My Name is {self.name}! from repr"
  
  def __len__(self):
    i = 0
    for c in self.name:
      i += 1
    return i
    
p3 = Employee("Haseeb Khan")
print(len(p3))

'''
__call__ method
The call method is used to make an object callable, meaning that 
you can pass it as a parameter to a function and it will be executed when 
the function is called. This is an incredibly powerful tool that allows you 
to create objects that behave like functions.
'''

#* Quick Quiz
class Employee:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return f"My Name is {self.name}! from str"
  
  def __repr__(self):
    return f"My Name is {self.name}! from repr"
  
  def __len__(self):
    i = 0
    for c in self.name:
      i += 1
    return i
  
  def __call__(self, *args, **kwds):
    #? generate automatically id when the instance is created
    self.id = "".join(
            random.choices(self.name + string.ascii_letters + string.digits, k=6)
        )
    print(f"The Employee's ID: {self.id}")
    

p4 = Employee("Haseeb Khan")
p4()