'''
Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to 
limit the access of class variables and class methods outside of class 
while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers

1: Public access modifier
2: Private access modifier
3: Protected access modifier
'''

# Public Access Specifier in Python
#? accessible from anywhere
class Student:
    #* constructor is defined
    def __init__(self, age, name):
        self.age = age               #* public variable
        self.name = name             #* public variable
obj = Student(21,"Harry")

print(obj.name)
print(obj.age)

#* Private Access Modifier
#? only accessible inside the class
class Student: 
  def __init__(self, age, name): 
      self.__age = age      # An indication of private variable
      self.__name = name      # An indication of private variable
  def __funName(self):  # An indication of private function
      self.y = 34
      print(self.y)
class Subject(Student):
    pass
  
obj = Student(21,"Harry")
obj1 = Subject

#! calling by object of class Student
# print(obj.__age)
# print(obj.__funName())
#! calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

#! Error
'''
AttributeError: 'student' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
AttributeError: 'subject' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
'''

'''
Name mangling

Name mangling in Python is a technique used to protect class-private 
and superclass-private attributes from being accidentally overwritten 
by subclasses. Names of class-private and superclass-private attributes 
are transformed by the addition of a single leading underscore and a double leading underscore respectively.
'''

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) #! Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

#* Protected Access Modifier
#? class that is intended to be accessed only by the class itself and its subclasses.

class Student:
    def __init__(self):
        self._name = "Harry"
    def _funName(self):      # protected method
        return "CodeWithHarry"
class Subject(Student):       #inherited class
    pass
  
obj3 = Student()
obj4 = Subject()

# calling by object of Student class
print(obj3._name)      
print(obj3._funName())   
# calling by object of Subject class
print(obj4._name)      
print(obj4._funName())   
