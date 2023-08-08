'''
Instance vs class variables

In Python, variables can be defined at the class level or at the instance level. 
Understanding the difference between these types of variables is crucial for 
writing efficient and maintainable code.
'''

class Employee:
  #? class variables
  #? Common and global for all instances in this class
  imClassVar = "Yes Class"
  noOfEmployees = 0
  def __init__(self, name):
    #? Instance
    self.name = name
    self.raise_amount = 0.02
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.imClassVar} is {self.raise_amount}")

emp1 = Employee("Haseeb")
emp1.raise_amount = 0.78
emp1.imClassVar = "Yes_its_Class_Changed" 
emp1.showDetails()
Employee.imClassVar = "Google"
print(Employee.imClassVar)

emp2 = Employee("Rohan")
emp2.imClassVar = "Nestle"
emp1.raise_amount = 0.78
emp2.showDetails()