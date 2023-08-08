'''
Set Methods:

Joining Sets
Sets in python more or less work in the same way as sets in mathematics. 
We can perform operations like union and intersection on the sets just like in mathematics.
'''

'''
union() and update():

The union() and update() methods prints all items that are present in the two sets. 
The union() method returns a new set whereas update() method adds item into the existing set from another set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2) #Returns new set of cities

print(cities)
print(cities2)
print(cities3)
print("********************************")
cities.update(cities2) #Update the existing set of cities
print(cities)
print(cities2)


'''
intersection and intersection_update():

The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
'''

print("********************************")
cities3 = cities.intersection(cities2) #Extract the matched cities and create a new set
print(cities3)

cities.intersection_update(cities2) #Extract the matched cities and update the existing set
print(cities)

'''
symmetric_difference and symmetric_difference_update():

The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
'''

print("********************************")
cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities6 = cities4.symmetric_difference(cities5) #Extract the not matched cities and create a new set
print(cities6)

cities4.symmetric_difference_update(cities5) #Extract the not matched cities and update the existing set
print(cities4)

'''
difference() and difference_update():

The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
'''
print("********************************")
cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities8 = {"Seoul", "Kabul", "Delhi"}

cities9 = cities7.difference(cities8) #Extract the only items that are only present in the original set and create a new set
print(cities9)

cities7.difference_update(cities8) #Extract the only items that are only present in the original set and update the existing set
print(cities7)

'''
Other Methods of sets

Set Methods:
There are several in-built methods used for the manipulation of set.They are 
explained below

1: isdisjoint():
The isdisjoint() method checks if items of given set are present in another
set. This method returns False if items are present, else it returns True.

2: issuperset():
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

3: issubset():
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

4: add()
If you want to add a single item to the set use the add() method.

5: update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

6: remove()/discard()
We can use remove() and discard() methods to remove items form list.

Note: The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

7: pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

8: del
del is not a method, rather it is a keyword which deletes the set entirely.

9: clear():
This method clears all items in the set and prints an empty set.

'''
print("****************Other Methods****************")
test1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
test2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print("****************isdisjoint****************")
print(test1.isdisjoint(test2)) #False
print("****************issuperset****************")
print(test1.issuperset(test2)) #False
print("****************issubset****************")
print(test1.issubset(test2)) #False
print("****************add****************")
print(test1.add('Lahore')) #{'Tokyo', 'Delhi', 'Madrid', 'Lahore', 'Berlin'}
print(test1)
print("****************update****************")
print(test1.update(test2)) #{'Tokyo', 'Delhi', 'Lahore', 'Berlin', 'Seoul', 'Kabul', 'Madrid'}
print(test1)
print("****************remove()/discard()****************")
# print(test1.remove('Pakistan')) #! Error: KeyError: 'Pakistan'
print(test1.discard('Pakistan')) # "None": Nothing happens if not present
print(test1.discard('Lahore')) # "None": remove Lahore from set
print(test1)
print("****************pop****************")
item = test1.pop()
print(item)
print(test1)

print("****************del****************")
cities10 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities10
# print(cities10) #! Error: NameError: name 'cities10' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

print("****************clear****************")
cities10 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities10.clear()
print(cities10) #set()