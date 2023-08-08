'''
Write a python program to translate a message into secret code language. 
Use the rules below to translate normal English into secret code language
 Coding:
  if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end
 else:
   simply reverse the string

 Decoding:
  if the word contains less than 3 characters, reverse it
 else:
  remove 3 random characters from start and end. Now remove the last letter
  and append it to the beginning

 Your program should ask whether you want to code or decode
'''
import string
import random

# generating random strings
def rendomStrGenerators(length):
  res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
  return str(res)

# encode the string
def encodeString(word):
  if len(word) >= 3:
    return rendomStrGenerators(3) + word[1:] + word[0] + rendomStrGenerators(3)
  else:
    return word[::-1] # reverse the word

# decode the string
def decodeString(word):
  if len(word) < 3:
    return word[::-1] # reverse the word
  else:
    return word[-4:-3]+ word[3:-4]

options = {"a": "Encode", "b": "Decode"}

print(f"Please select your option: \n")
for key, value in options.items():
 print(f"{key}: {value}")

value = input("options: ")
if(value.lower() == 'a'):
  userEnInput = input("Enter the word to encode: ")
  en = encodeString(userEnInput)
  print("The Encoded String is (Copy the String): ", en)
elif(value.lower() == 'b'):
  userDeInput = input("Enter the word to decode: ")
  de = decodeString(userDeInput)
  print("The Decoded String is: ", de)
else:
  raise ValueError("Invalid Input!")