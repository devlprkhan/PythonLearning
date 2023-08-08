'''
Inheritance in python

When a class derives from another class. 
The child class will inherit all the public and protected properties and 
methods from the parent class. In addition, 
it can have its own properties and methods,this is called as inheritance.
'''

class Father:
   def func1(self):
        print("This function is in parent class.")

# ?Inherit from the parent class
class Son(Father):
   def func2(self):
        print("This function is in child class.")
        
f1 = Father();
f1.func1()
f2 = Son();
f2.func2()

# Multiple Inheritance:
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Haseeb"
s1.mothername = "I don't know"
s1.parents()
