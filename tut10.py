'''
Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times.
This can be done using loops. 
Based on this loops are further classified into following main types;

for loop
while loop
'''

# string
name="Haseeb"
# List
colors=["white", "black", "orange", "green", "violet"]

for char in name:
  print(char, end=' ,')

# Nested loop
for color in colors:
  print(color)
  for char in color:
    print(char)
    
'''
range():
What if we do not want to iterate over a sequence? 
What if we want to use for loop for a specific number of times?
**Note** that it skips the last index for example: 1 to 5: 1,2,3,4
'''

for num in range(1, 300):
  print(num+1) #to also add the last index i plus 1
  
'''
while Loop
As the name suggests, while loops execute statements while the condition is True. 
As soon as the condition becomes False, 
the interpreter comes out of the while loop.
'''

print('""""""""""""""""""""while loop""""""""""""""""""""""')
n=0
while (n < 5):
  print(n);
  n += 1

# Revers loop
n1 = 10
while (n1 > 0):
  print(n1)
  n1 = n1 - 1
  
'''
Else with While Loop
We can even use the else statement with the while loop. 
Essentially what the else statement does is that as soon as the while loop condition becomes False, 
the interpreter comes out of the while loop and the else statement is executed.
'''

# also use the else with the loop below
n2 = 0
while (n2 < 5):
  print("In the loop: ", n2)
  n2 += 1
else:
  print("In the else: ", n2)
print('""""""""""""""""""""""""""""""""""""""""""')

print('"""""""""""""""""""""Emulating do-while loop"""""""""""""""""""""')

'''
How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a 
bit in order to get similar behavior to a do while loop.
'''

while True:
 entered_number = int(input("Enter positive number: "))
 print('Entered number is: ', entered_number)
 if (not entered_number > 0):
   break

print("Outside the emulated do-while loop")
print('""""""""""""""""""""""""""""""""""""""""""')


