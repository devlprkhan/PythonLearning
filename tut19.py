'''
String formatting in python

String formatting can be done in python using the format method.
'''
str = "My Name is {} and My Email is {}"
print(str.format("Haseeb Khan", "devlpr.khan@gmail.com"))

'''
f-strings in python

It is a new string formatting mechanism introduced by the PEP 498. 
It is also known as Literal String Interpolation or more commonly 
as F-strings (f character preceding the string literal). 
The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', 

the string becomes the f-string itself. 
The f-string can be formatted in much same as the str.format() method.
The f-string offers a convenient way to embed Python expression inside 
string literals for formatting.
'''

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Haseeb'  
print(f"Hellow I'm {name}!")
# Also perfrom calculations
print(f"{2 * 30}")

# To print the {} in f string we use double {{}}
print(f"Hellow I'm {{name}}!") #Hellow I'm {name}!