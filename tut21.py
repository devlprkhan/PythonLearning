'''
Recursion in python
Recursion is the process of defining something in terms of itself.

Python Recursive Function

In Python, we know that a function can call other functions. 
It is even possible for the function to call itself. 
These types of construct are termed as recursive functions.
'''

def factorial(number):
  if(number == 0 or number == 1):
    return number
  else:
    return (number * factorial(number-1))
  
# print(factorial(5))

# Steps
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# 120

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

def fibonacci(x):
  if (x <= 1):
    return x
  else:
    return fibonacci(x-1)+fibonacci(x-2)
  
print(fibonacci(10))