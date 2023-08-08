'''
Operator Overloading in Python: An Introduction

Operator Overloading is a feature in Python that allows developers to redefine 
the behavior of mathematical and comparison operators for custom data types. 
This means that you can use the standard mathematical 
operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) 
in your own classes, just as you would for built-in 
data types like int, float, and str.

# Dunder method of Operators
+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__
'''
#? the Operator Overloading means we can change the actual function of operator like:
# ? with help of Dunder function we change the actual functionality of function
#* like: + --> __add__ (adds 2 arguments)
#* but we can change him to subtract

class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
  def __add__(self, x):
    return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Vector(10, 15, 16)
print(v1)

v2 = Vector(10, 20, 90)
print(v2)

#* if we cannot define custom logic for (+ Or __add__) we got this error:
#! unsupported operand type(s) for +: 'Vector' and 'Vector'
# else:
'''
10i + 15j + 16k
10i + 20j + 90k
---------------
20i + 35j + 106k
'''
print(v1 + v2)
print(type(v1 + v2)) #<class '__main__.Vector'>
