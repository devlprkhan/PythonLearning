'''
Python Lists

Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.
'''

lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = ['Red', 'Green', 'Blue', 'Yellow']
details = ["Abhijeet", 18, "FYBScIT", 9.8]

print('List 1: ', lst1)
print('List 2: ', lst2)
print('List 3: ', details)

'''
List Index

Each item/element in a list has its own unique index. 
This index can be used to access any particular item from the list. 
The first item has index [0], second item has index [1], third item has index [2] and so on.
'''

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

'''
Accessing list items

We can access list items by using its index with the square bracket syntax []. 
For example colors[0] will give "Red", colors[1] will give "Green" and so on...
'''

print(colors[2])
print(colors[4])
print(colors[0])
print('""""""""""""""""""""""""""""""""""""""""""')

'''
Negative Indexing:

Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. 
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
'''

print(colors[-1]) #len(colors)-1 => 5-1 => 4 => "Green"
print(colors[-3]) #len(colors)-3 => 5-3 => 2 => "Blue"
print(colors[-5]) #len(colors)-5 => 5-5 => 0 => "Red"
print('""""""""""""""""""""""""""""""""""""""""""')

'''
Check whether an item in present in the list?

We can check if a given item is present in the list. 
This is done using the "in" keyword.
'''

if "Green" in colors:
  print("Yes its present in the list")
else:
  print("No its not present in the list")
  
# Also work on "strings"
str = "Haseeb"

if "eib" in str:
  print("Yes its present in the string")
else:
  print("No its not present in the string")
  
print('""""""""""""""""""""""""""""""""""""""""""')

'''
Range of Index:

You can print a range of list items by specifying where you want to start,
where do you want to end and if you want to skip elements in between the range.
'''
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

# printing all element from a given index till the end
print(animals[3:])	#using positive indexes
print(animals[-4:])	#using negative indexes

# printing all elements from start to a given index
print(animals[:4])  #using positive indexes
print(animals[:-5])  #using negative indexes

#printing every 3rd consecutive value withing a given range

print(animals[1:8:3])
# Here, jump index is 3. Hence it prints every 3rd element within given index.
# print elements from every 3rd consecutive value withing a given range
print(animals[::3])
print('""""""""""""""""""""""""""""""""""""""""""')

'''
List Comprehension

List comprehensions are used for creating new lists from 
other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

Syntax:
List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.
Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
Condition: Condition checks if the item should be added to the new list or not.
'''
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameWith_O = [name for name in names if "o" in name]
print(nameWith_O)

# Accepts items which have more than 4 letters
nameWithMorethan_4 = [moreThan4Word for moreThan4Word in names if len(moreThan4Word) > 4]
print(nameWithMorethan_4)
print('""""""""""""""""""""""""""""""""""""""""""')