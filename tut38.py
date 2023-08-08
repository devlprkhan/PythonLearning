'''
Map, Filter and Reduce

In Python, the map, filter, and reduce functions are
built-in functions that allow you to apply a function to a sequence
of elements and return a new sequence. 
These functions are known as higher-order functions, 
as they take other functions as arguments.
'''
defList = [1,2,3,4,5,6,7,8,9,10,11,12]

# map
triplet = list(map(lambda x: x*x*x, defList)) #cube
print(triplet)

# filter
even = list(filter(lambda x: x%2==0, defList)) #extract even
print(even)

# reduce
# we need to import reduce
from functools import reduce

wholeSum = reduce(lambda x,y: x+y, defList) #whole sum of list (78)
print(wholeSum)

'''
'is' vs '==' in Python
In Python, is and == are both comparison operators 
that can be used to check if two values are equal. 
However, there are some important differences between the two that 
you should be aware of.

The is operator compares the identity of two objects, 
while the == operator compares the values of the objects. 
This means that is will only return True if the objects being compared
are the exact same object in memory, while == will return True if 
the objects have the same value.
'''

#! Note that everything which is constant in Python returns True on both (is, ==) unless you change the constant

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

#* value
print(list1 == list2) #True
#* exact location of object in memory
print(list1 is list2) #False

a = 'A'
b= 'A'

#* because its constant and python did not create same constant again and again unless you change it
print(a == b) #True
print(a is b) #True

#* Tuples is also immutable (constant)
tup1=(1,2)
tup2=(1,2)

print(tup1 == tup2) #True
print(tup1 is tup2) #True

a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value