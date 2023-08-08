'''
break statement
The break statement enables a program to skip over a part of the code. 
A break statement terminates the very loop it lies within.
'''

# *Printing the 8 table with loop & break statements
tableOf=8
for devider in range(12):
  if (devider == 11):
    print("Inside break statement")
    break;
  print(tableOf, " X ", devider, " = ", tableOf*devider)

print("Outside of loop with break statement")
print('""""""""""""""""""""""""""""""""""""""""""')
'''
Continue Statement
The continue statement skips the rest of the 
loop statements and causes the next iteration to occur.
'''
# *Printing the 10 table with loop & continue statements
tableOf=10
for devider in range(12):
  if (devider == 11 or devider == 0): #skips the 0, 11 line
    print("Inside continue statement")
    continue;
  print(tableOf, " X ", devider, " = ", tableOf*devider)

print("Outside of loop with continue statement")
