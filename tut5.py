'''
What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. 
A string is essentially a sequence or array of textual data. 
Strings are used when working with Unicode characters.
'''

str1 = "Haseeb"
str2 = 'Haseeb khan 2'

# Multiline string
str3 = '''
In python, anything that you enclose between single or double

quotation marks is considered a string. 

A string is essentially a sequence or array of textual data
'''

print(str1)
print(str2)
print(str3)

# Accessing the Index (Because in Python the string is "like" array)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])


# Through loop (Big String)
for character in str3:
    print(character)


# *Strings Slicing and Operations on Strings
# ?Quick Quiz Solution
# *Question (Output)?
str4 = "Harry"
print(str4[-4:-2])  # * => ar (Note: the last index should not be quoted or ignored)

'''
Length of a String
We can find the length of a string using len() function.
'''

str5 = "Mango"
print("The length of", str5, "is: ", len(str5))

'''
String as an array
A string is essentially a sequence of characters also called an array. 
Thus we can access the elements of this array.
'''
str6 = "Haseeb"  # Last index value has been ignored
print(str6[1])  # a
print(str6[0:3])  # Has
print(str6[:3])  # Has (The "0" is automatically added)
# Haseeb (This will automatically prints till the end of string length)
print(str6[:])
print(str6[-5:-4])  # output: "a"
print(str6[-4:])  # output: seeb => Slicing using negative index

# Explanation of (str6[-5:-4])
'''
Haseeb => 6
str6[len(str6)-5:len(str6)-4]
str6[6-5:6-4]
str6[1:2]
Ans: a
'''

# Slicing Example:
