'''
Python Tuples
Tuples are ordered collection of data items. 
They store multiple items in a single variable. Tuple items are separated by commas
and enclosed within round brackets (). 

Tuples are unchangeable meaning we can not alter them after creation.

Note: ***This is same as lists, except its not mutated or changed
'''

tup1 = (1, 2, 3)
tup2 = ('red', 'green', 'blue', 'yellow')
print(tup1, '\n',tup2)

'''
Tuple Indexes

Each item/element in a tuple has its own unique index. 
This index can be used to access any particular item from the tuple. 
The first item has index [0], second item has index [1], third item has index [2] and so on.
'''

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
print(country[0])
print(country[1])
print(country[2])
print('*********************************')

'''
Negative Indexing:

Similar to positive indexing, negative indexing is also used
to access items, but from the end of the tuple. 
The last item has index [-1], second last item has index [-2], 
third last item has index [-3] and so on.
'''

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
# print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
print('*********************************')

'''
Check for item:
We can check if a given item is present in the tuple. 
This is done using the in keyword.
'''
country = ("Spain", "Italy", "India", "England", "Germany")

if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
    
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
print('*********************************')

'''
Range of Index:

You can print a range of tuple items by specifying where do you want to start, 
where do you want to end and if you want to skip elements in between the range.
'''

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

# *And the method used as well as the in the list .....