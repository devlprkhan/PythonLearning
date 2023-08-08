'''
Taking User Input in python
In python, we can take user input directly by using input() function.This input
function gives a return value as string/character hence we have to pass that
into a variable
'''
xx=input("Enter Your Name Sir: ")
print("Your Name is: ", xx)

x=input("Enter 1st Num: ")
y=input("Enter 2nd Num: ")

print("The sum of 1st & 2nd is: ", int(x)+int(y))

print("===============TODO Task Solution==================")
a=input("Enter 1st Number: ")
b=input("Enter 2nd Number: ")

print("================Answer=================")
print("The Value of", a, "and", b, "after \"addition\": ", int(a)+int(b))
print("The Value of", a, "and", b, "after \"subtraction\": ", int(a)-int(b))
print("The Value of", a, "and", b, "after \"multiplication\": ", int(a)*int(b))
print("The Value of", a, "and", b, "after \"division\": ", int(a)/int(b))
print("The Value of", a, "and", b, "after \"Modulus\": ", int(a)%int(b))
print("The Value of", a, "and", b, "after \"Floor Division\": ", int(a)//int(b))
print("The Value of", a, "and", b, "after \"Exponential\": ", int(a)**int(b))
print("=================================")
