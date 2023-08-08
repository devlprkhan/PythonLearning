'''
A match statement will compare a given variable’s value to different shapes, 
also referred to as the pattern. The main idea is to keep on comparing the variable 
with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, 
a condition to be evaluated if the pattern matches, 
and a set of statements to be executed if the pattern matches.
'''
x=3
match x:
  case 1:
    print("match keyword 1")
  case 2:
    print("match keyword 2")
  case 3:
    print("match keyword 3")
  case _ if x < 5: #also add if keyword 
    print("match keyword default <5")
  case _: #default case
    print("match keyword default")