'''
Python Dictionaries

Dictionaries are ordered collection of data items. 
They store multiple items in a single variable. 
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)#{'name': 'Karan', 'age': 19, 'eligible': True}
print(info['age'])#19
print(info.get('age'))#19 

# Both are same but there is a catch the "info['age']" throws exception if it 
# is not exists els the "info.get('age')" give None if it is not exists
# print(info['red'])#! KeyError: 'red'
print(info.get('red'))#None 


'''
Accessing multiple values:
We can print all the values in the dictionary using values() method.
'''
print(info.values())
'''
Accessing keys:
We can print all the keys in the dictionary using keys() method.
'''
print(info.keys())
'''
Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.
'''
print(info.items())
# or
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
