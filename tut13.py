'''
Function Arguments and return statement
There are four types of arguments that we can provide in a function:

Default Arguments
Keyword Arguments
Variable length Arguments
Required Arguments
'''

'''
Default arguments:
We can provide a default value while creating a function. This way the function
assumes a default value even if a value is not provided in the function call for that argument.
'''
def funcWithDefArgs(a=10, b=20):
  print("The sum of the arguments is: ", a+b)

funcWithDefArgs()

'''
Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes
the arguments by the parameter name. Hence, the the order in which the 
arguments are passed does not matter.
'''
def funcWithKeywordArgs(a=10, b=20):
  print("Fuction with keyword arguments: (Sum of the arguments): ", a+b)
  
funcWithKeywordArgs(b=30) #Place at the position of "b"

'''
Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is 
necessary to pass the arguments in the correct positional order and the number 
of arguments passed should match with actual function definition.
'''
def funcWithRequiredArgs(req, noReq1=20, noReq2=30):
  print("Function With Required Args: ", noReq1, noReq2, req)
  
# funcWithRequiredArgs(noReq1=10, noReq2=10) # !funcWithRequiredArgs() missing 1 required positional argument: 'req'
funcWithRequiredArgs(req=20)

'''
Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual
function. This can be done using variable-length arguments.

There are two ways to achieve this:
'''

'''
Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
'''
def funcGetTheAverage(*numbers):
  sum=0
  for i in numbers:
    sum = sum+i
  print("The Average of the arguments is: ", sum / len(numbers))

funcGetTheAverage(5,6,7,8,9) # * Pass arguments as many as possible (Take as a Tupple)
'''
Keyword Arbitrary Arguments:
While creating a function, pass a ** before the parameter name while defining 
the function. The function accesses the arguments by processing them in the 
form of dictionary.
'''
def name(**name):
    print("Hello,", name["firstName"], name["mname"], name["lname"])
    
name(mname = "Ul", lname = "Hassan", firstName = "Haseeb")


'''
return Statement
The return statement is used to return the value of the expression back to the 
calling function.
'''

def funcToReturnName(name="Khan"):
  return name.title() #Returns Name with Capitilized Name

myName = funcToReturnName("haseeb khan")
print("My name is " + myName)