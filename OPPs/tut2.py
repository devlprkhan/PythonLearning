'''
Constructors
A constructor is a special method in a class used to create and 
initialize an object of a class. There are different types of constructors. 
Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an 
object is created of a class. The main purpose of a constructor is to 
initialize or assign values to the data members of that class. 
It cannot return any value other than None.

Types of Constructors in Python

1: Parameterized Constructor
2: Default Constructor
'''

# 1: Parameterized Constructor
# Constructors is a nothing but a pass parameter to the class
class PersonWithConstructorParam:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation
    
  def info(self):
    print(f"{self.name} is an {self.occupation} person")

#? Note: that the "self" parameter is passed to the class by default
p1 = PersonWithConstructorParam("Haseeb", "Developer")

#? Errors
# p1 = PersonWithConstructorParam("Haseeb") #! missing 1 required positional argument: 'occupation'
# p1 = PersonWithConstructorParam("Haseeb", "Developer", 1) #! TypeError: PersonWithConstructorParam.__init__() takes 3 positional arguments but 4 were given

p1.info()

# 2: Default Constructor
class PersonWithConstructor:
  name = "Haseebo"
  occupation = "Rider"
  def __init__(self):
    print("I'm a constructor and I'm Calling Every time when the object is created")

  def info(self):
    print(f"{self.name} is an {self.occupation} person")

p2 = PersonWithConstructor()
p2.info()