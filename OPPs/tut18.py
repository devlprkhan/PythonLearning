'''
Inheritance in Python
'''

'''
Single Inheritance in Python

Single inheritance is a type of inheritance where a class inherits properties 
and behaviors from a single parent class. This is the simplest and most common 
form of inheritance.
'''
print("=================Single Inheritance================")
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    
  def makeSound(self):
    print("Sound mande by animal!")
    
  def callChildrenMethod(self, child_instance):
    print("Calling children method from parent!")
    child_instance.eat()
    
#* The Cat class inherits from Animal class
class Cat(Animal):
  def __init__(self, name, species, breed):
    super().__init__(name, species)
    self.breed = breed
  
  def makeSound(self):
    print("Sound: meow!")
    
  def eat(self):
    print("Eating rats!")
    
  def sleep(self):
    print("Sleeping 20 hours a day!")
  
animal = Animal("animal", "general")  
animal.makeSound()
cat = Cat("caty", "cat", "persion")
cat.makeSound()
cat.eat()
cat.sleep()

animal.callChildrenMethod(cat)

'''
Multiple Inheritance in Python

Multiple inheritance is a powerful feature in object-oriented programming that
allows a class to inherit attributes and methods from multiple parent classes. 
This can be useful in situations where a class needs to inherit functionality 
from multiple sources.
'''
print("=================Multiple Inheritance================")
class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
   def __init__(self, dance, name):
    self.dance = dance
    self.name = name
    
dancer_employee = DancerEmployee("Salsa", "John Doe")
print(dancer_employee.name)
print(dancer_employee.dance)
dancer_employee.show()
print(DancerEmployee.mro())

'''
Multilevel Inheritance in Python

Multilevel inheritance is a type of inheritance in object-oriented programming
where a derived class inherits from another derived class. This type of 
inheritance allows you to build a hierarchy of classes where one class 
builds upon another, leading to a more specialized class.

like: grandparent ---> parent ---> child
'''
print("=================Multilevel Inheritance================")
class Animal2:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog2(Animal2):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal2.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog2):
  def __init__(self, name, color):
    Dog2.__init__(self, name, breed="Jerman Shefered")
    self.color = color
    
  def show_details(self):
    Dog2.show_details(self)
    print(f"Color: {self.color}")
    
dog = GoldenRetriever("Max", "Dark Brown")
dog.show_details()
print(GoldenRetriever.mro())

'''
Hybrid Inheritance in Python

Hybrid inheritance is a combination of multiple inheritance and single 
inheritance in object-oriented programming. It is a type of inheritance in which
multiple inheritance is used to inherit the properties of multiple base classes
into a single derived class, and single inheritance is used to inherit the properties 
of the derived class into a sub-derived class.
'''

print("=================Hybrid Inheritance================")

class BaseClass1:
  # attributes and methods
  pass
class BaseClass2:
  # attributes and methods
  pass
class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods
  pass

class FinalClass(DerivedClass):
  pass

'''
Hierarchical Inheritance

Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming
where multiple subclasses inherit from a single base class. In other words, 
a single base class acts as a parent class for multiple subclasses. 
This is a way of establishing relationships between classes in a 
hierarchical manner.
'''

print("=================Hierarchical Inheritance================")
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass

class D4(D2):
  pass