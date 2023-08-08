'''
Python Class and Objects

A class is a blueprint or a template for creating objects, 
providing initial values for state (member variables or attributes), 
and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.

self parameter
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.
'''
# Blueprint
class Person:
    # Default parameters
    name= "Shifa"
    age= 22
    occupation= "Teller"

    def info(self):
        print(
            f"Name: {self.name} and age: {self.age}, and occupation is: {self.occupation}")


# With the default parameters
person0 = Person()
person0.info()

# Create an object of class
person1 = Person()
person1.name = "Haseeb Khan"
person1.age = 18
person1.occupation = "Rider"
person1.info()

a = Person()
b = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
