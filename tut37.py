'''
Lambda Functions in Python
In Python, a lambda function is a small anonymous function without a name. 
It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

Lambda functions are often used in situations where a 
small function is required for a short period of time. 
They are commonly used as arguments to higher-order functions, 
such as map, filter, and reduce.

Here is an example of how to use a lambda function:
'''
#* One liner for short function
square1 = lambda x: x*x
# Other way
def square2(x):
    return x*x

print("Squre: ",square1(4))

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x*y*z)/3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
# Also pass the function as argument to another function
print(appl(lambda x: x * x , 2))