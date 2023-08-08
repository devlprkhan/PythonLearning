'''
Super keyword in Python

The super() keyword in Python is used to refer to the parent class. 
It is especially useful when a class inherits from multiple parent classes 
and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the 
methods defined in the parent class. However, sometimes you might want to 
use the parent class method in the child class. This is where the 
super() keyword comes in handy.
'''

#? super() is nothing but a keyword used to refer to the parent class
#* Old way of doing things we pass parameters multiple times in Parent & Child its same
class Parent:
  def __init__(self, name, age):
    self.name = name,
    self.age = age
  
  def display(self):
    print("I'm in a parent class!")
    
class Child(Parent):
  def __init__(self, family, name, age):
    self.family = family,
    self.name = name,
    self.age = age

  def displayChild(self):
    print("I'm in a child class!")
    
p1 = Parent("AbdulSabeer", "50")
print(p1.name)
print(p1.age)
p1.display()
p2 = Child("Abdul Sabeer", "Haseeb", "22")
print(p2.family)
print(p2.name)
print(p2.age)
p2.displayChild()

#* New way simply use the super() keyword and merge the Parent constructor with the child constructor
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    #* Also add the Employee Construct in Programmer constructor
    super().__init__(name, id)
    self.lang = lang
    
h1 = Employee("Muneeb", "894798")
h2 = Programmer("Haseeb", "3737", "Python")
print(h2.name)
print(h2.id)
print(h2.lang)