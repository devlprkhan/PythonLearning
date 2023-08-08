'''
String methods
Python provides a set of built-in methods 
that we can use to alter and modify the strings.
'''

print("==================String Methods==================")
# upper() :
# The upper() method converts a string to upper case.
print("==============Upper==============")
str1 = " AbcDEfghIJ jhjkh \n 6678 !!!"
print(str1.upper())
print("==============Lower==============")
print(str1.lower())
print("==============Capitalize==============")
'''
capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 
The string has no effect if the first character is already uppercase.
'''
print(str1.capitalize())
print("==============Strip==============")
'''
strip() :
The strip() method removes any white spaces before and after the string.
'''
print(str1.strip())
print("==============Rstrip==============")
'''
rstrip() :
the rstrip() removes any trailing characters. Example:
'''
print(str1.rstrip('!'))
print("==============Replace==============")
'''
replace() :
The replace() method replaces all occurences of a string with another string.
'''
print(str1.replace('A', 'Haseeb'))
print("==============Split==============")
'''
split() :
The split() method splits the given string at the specified 
instance and returns the separated strings as list items.
'''
print(str1.split(' '))
print("==============Center==============")
'''
center() :
The center() method aligns the string to the
center as per the parameters given by the user.
'''
print(str1.center(100))
print(str1.center(100, '.'))
print("==============Count==============")
'''
count() :
The count() method returns the number of times the given 
value has occurred within the given string.
'''
print(str1.count('A'))
print("==============Endswith==============")
'''
endswith() :
The endswith() method checks if the string ends with a given value. 
If yes then return True, else return False.
'''
print(str1.endswith('!')) #true
print(str1.endswith(')')) #false
print("==============Find==============")
'''
find() :
The find() method searches for the first occurrence of the given value and returns the index where it is present. 
If given value is absent from the string then return -1.
'''
print(str1.find('!')) #23
print(str1.find(')')) #-1
print("==============Index==============")
'''
index() :
The index() method searches for the first occurrence of 
'''
print(str1.index('!')) #23
# print(str1.index(')')) #!ValueError: substring not found
print("==============Isalnum==============")
'''
isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
If any other characters or punctuations are present, 
then it returns False.
'''
print(str1.isalnum()) #False
print("==============Isalpha==============")
'''
isalpha() :
The isalnum() method returns True only if the entire string only
consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present,
then it returns False.
'''
print(str1.isalpha()) #False
print("==============Islower==============")
'''
islower() :
The islower() method returns True if 
all the characters in the string are lower case, else it returns False.
'''
print(str1.islower()) #False
print("==============Isprintable==============")
'''
isprintable() :
The isprintable() method returns True if all the values within 
the given string are printable, if not, then return False.
'''
print(str1.isprintable()) #False because of (\n: escape sequence character which is not printable)
print("==============Isspace==============")
'''
isspace() :
The isspace() method returns True 
only and only if the string contains white spaces, else returns False.
'''
str3 = "        "       #using Spacebar
print(str3.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
print("==============Istitile==============")
'''
istitle() :
The istitile() returns True only if the first letter of each word
of the string is capitalized, else it returns False.
'''
str10 = "World Health Organization" 

print(str1.istitle()) #False
print(str10.istitle()) #True
print("==============Isupper==============")
'''
isupper() :
The isupper() method returns True if all 
the characters in the string are upper case, else it returns False.
'''
str11 = "WORLD HEALTH ORGANIZATION" 
print(str11.isupper())
print("==============Startswith==============")
'''
startswith() :
The startswith() method checks if the string starts with a given value.
If yes then return True, else return False.
'''
str11 = "WORLD HEALTH ORGANIZATION" 
print(str11.startswith('WORLD'))
print("==============Swapcase==============")
'''
swapcase() :
The swapcase() method changes the character casing of the string.
Upper case are converted to lower case and lower case to upper case.
'''
str13 = "WORLD HEALTH ORGANIZATION" 
print(str13.swapcase())
print("==============Title==============")
'''
title() :
The title() method capitalizes each letter of the word within the string.
'''
str14 = "He's name is Dan. Dan is an honest man."
print(str14.title())
print("==================================================")