'''
List Methods

1: list.sort()
This method sorts the list in ascending order. The original list is updated

2: list.reverse()
This method reverses the order of the list.

3: list.index()
This method returns the index of the first occurrence of the list item.

4: list.count()
Returns the count of the number of items with the given value.

5: list.copy()
Returns copy of the list. This can be done to perform operations 
on the list without modifying the original list.

6: list.append():
This method appends items to the end of the existing list.

7: list.insert():
This method inserts an item at the given index. User has to specify index 
and the item to be inserted within the insert() method.

8: list.extend():
This method adds an entire list or any 
other collection datatype (set, tuple, dictionary) to the existing list.

9: Concatenating two lists:
You can simply concatenate two lists to join two lists.
'''

l = [11, 45, 1, 2, 4, 6, 1, 1]
print("Orignal List: ",l)

# 1: Sort
l.sort()
print(l)

# 2: Reverse
l.reverse()
print(l)

# 2nd Method
l.sort(reverse=True)
print(l)

# 3: Index
index = l.index(2)
print(index)

# 4: Count
count = l.count(1)
print(count)

# 5: Copy
copy = l.copy()
print(copy)

# 6: Append
l.append(786) # Append at last
print(l)

# 7: Insert
l.insert(1, 999999) # Insert at specified index
print(l)

# 8: Extend
newList = [0,0,0]
l.extend(newList) # Extend at last
print(l)

# 9: Concatenating
m = [900, 1000, 1100]
k = l + m
print(k)