'''
Python - else in Loop
As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. 
The else block appears after the body of the loop. The statements in the else 
block will be executed after all iterations are completed. 
The program exits the loop only after the else block is executed.
'''
# With for
for i in range(5):
  print(i)
else:
  print("The for Loop is finished successfully!") 
  #* Note: only executed when the loop is finished successfully
  
# With while loop
i=0
while i < 5:
  print(i)
  i+=1
else:
  print("The while Loop is finished successfully!")
  
# The fail case in which the else loop is not executed
for i in range(5):
  print(i)
  if(i == 3):
    break
else:
  print("This Else is Not Printing!, Because the loop is break and its not executed till last")