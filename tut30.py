'''
If ... Else in One Line

There is also a shorthand syntax for the if-else statement 
that can be used when the condition being tested is simple 
and the code blocks to be executed are short. 

Here's an example:
'''

a = 2
b = 330

print("A") if a > b else print("B") # B

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B") # =

'''
Enumerate function in python

The enumerate function is a built-in function in Python that allows
you to loop over a sequence (such as a list, tuple, or string) and get the 
index and value of each element in the sequence at the same time. 

Changing the start index

By default, the enumerate function starts the index at 0, but you can specify a different 
starting index by passing it as an argument to the enumerate function:
Here's a basic example of how it works:
'''
# ! old way of doing this
marks = [12, 56, 32, 98, 12,  45, 1, 4]

index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
  index +=1

#* New Way
# Loop through a tuple
colors = ('red', 'green', 'blue') 

for index, color in enumerate(colors):
  print(f"The name of color is {color} and the position is {index}")

# Loop through a list
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=2): # start index from 2 and onwards
    print(f'{index+1}: {fruit}')
    
# Loop over a string and print the index and value of each character
s = 'hello'
for index,char in enumerate(s):
  print(f"{index}: {char}")