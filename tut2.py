a=True
b="Haseeb"
c=1234
d=12.34
e=complex(10,20)
f=None

print("=================================")
print("The Value of a is: ", a)
print("The Value of b is: ", b)
print("The Value of c is: ", c)
print("The Value of d is: ", d)
print("The Value of e is: ", e)
print("The Value of f is: ", f)
print("=================================")

print("=================================")
print("The Type of a is: ", type(a))
print("The Type of b is: ", type(b))
print("The Type of c is: ", type(c))
print("The Type of d is: ", type(d))
print("The Type of e is: ", type(e))
print("The Type of f is: ", type(f))
print("=================================")

print("================Other Data & its Types=================")
list1 = [1,2,3,['Haseeb', 'Ameen'], 1.23,77,complex(90,70)]
print("The Value of list1 is: ", list1)

tuple1 = (1,23, ("Khan", "G"),(23.33,6))
print("The Value of tuple1 is: ", tuple1)

dict1 = {"Name": "Haseeb", "Age": 21, "CanVote": True}
print("The Value of dict1 is: ", dict1)

print("=================================")
print("The Type of list1 is: ", type(list1))
print("The Type of tuple1 is: ", type(tuple1))
print("The Type of dict1 is: ", type(dict1))
print("=================================")
print("=================================")

print("================Ex#1=================")
print('Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!')

a=4
b=2

print("================Ex#1 Solution=================")
print("The Value of", a, "and", b, "after \"addition\": ", a+b)
print("The Value of", a, "and", b, "after \"subtraction\": ", a-b)
print("The Value of", a, "and", b, "after \"multiplication\": ", a*b)
print("The Value of", a, "and", b, "after \"division\": ", a/b)
print("The Value of", a, "and", b, "after \"Modulus\": ", a%b)
print("The Value of", a, "and", b, "after \"Floor Division\": ", a//b)
print("The Value of", a, "and", b, "after \"Exponential\": ", a**b)
print("=================================")

