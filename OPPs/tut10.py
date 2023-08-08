'''
Python Class Methods: An Introduction

In Python, classes are a way to define custom data types that can store 
data and define functions that can manipulate that data. One type of function
that can be defined within a class is called a "method." In this blog post, 
we will explore what Python class methods are, why they are useful, and how to use them.
'''

#? Class Method is nothing but we can use to change class variables or methods inside the class instance

class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")
  @classmethod #? now with this i can change the company variable of class
  def changeCompany(self, newCompany):
    self.company = newCompany


e1 = Employee()
e1.name = "Haseeb"
e1.show()
e1.changeCompany("KHan")
e1.show()
print(Employee.company)