'''
Python Sets

Sets are unordered collection of data items. 
They store multiple items in a single variable. 
Set items are separated by commas and enclosed within curly brackets {}.
Sets are unchangeable, meaning you cannot change items of the set once created. 
Sets do not contain duplicate items.
'''

#remove the duplicates and the important note is that
#after removing he does not contain the order of the items
set1 = {1,2,3,4,5,6,7,8,9,9}
print(set1) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

info = {'Haseeb', 18, True, 18.5, 18.5}
print(info)
#for now the order is: {True, 18, 18.5, 'Haseeb'} maybe its change on next rendering

'''
Quick Quiz: 

Try to create an empty set. Check using the type() function whether
the type of your variable is a set
'''

set2 = {}
print(type(set2)) #Wrong: its dict because empty currently brackets consider as dictionary

set3 = set()
print(type(set3)) #Correct: its set

# Accessing the items of the set
for item in info:
  print(item)