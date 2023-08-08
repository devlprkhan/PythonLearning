'''
Regular Expressions in Python

Regular expressions, or "regex" for short, are a powerful tool for working with 
strings and text data in Python. They allow you to match and manipulate strings 
based on patterns, making it easy to perform complex string operations with
just a few lines of code.

Metacharacters in regular expressions
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
'''

import re

# Define a regular expression pattern
pattern = r"[A-Za-z]ello"

# Match the pattern against a string
text = "Hello, world!, hello, world"

match = re.findall(pattern, text)
print("Results:", match)

if match:
    print("Match found!", match)
else:
    print("Match not found.")
    
text = "The email address is example@example.com."
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    email = match.group()
    print(email)