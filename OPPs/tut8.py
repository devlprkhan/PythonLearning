'''
Static methods

Static methods in Python are methods that belong to a class rather than an
instance of the class. They are defined using the @staticmethod decorator 
and do not have access to the instance of the class (i.e. self).
They are called on the class itself, not on an instance of the class. 
Static methods are often used to create utility functions that don't need access to instance data.
'''

#? Static methods can be defined inside a class but can use any where without using the "self" keyword its a global
class Math:
  def __init__(self, num):
    self.num = num
  def addtonum(self, n):
    self.num = self.num +n
  @staticmethod
  def add(a,b):
    return a+b
  
a = Math(5)
print(a.num) #5
a.addtonum(6)
print(a.num) #11
print(Math.add(10,10))
