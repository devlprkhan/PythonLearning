'''
if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), 
whether the expression(s) evaluate to True or False. If the expression evaluates to False, 
then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

if
if-else
if-else-elif
nested if-else-elif.
'''

num = 18

print("==================if-else Statements==================")
print("==============if==============")

if(num >= 18):
  print("Hi I'm 18")
  
print("==============if-else==============")

if(num < 18):
  print("No")
else:
  print('Yes')

print("==============if-else-elif==============")

num1 = 19
num2 =20

if(num1 <= 10):
  print("Hi Hello! I'm Not Printing")
elif(num1 < num2):
  print("I'm Printing!")
else:
  print("All Fail! in Printing")
  
print("==============nested if-else-elif==============")

if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num >= 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

print("==================================================")