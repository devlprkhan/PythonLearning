'''
Generators in Python

Generators in Python are special type of functions that allow you to create an
iterable sequence of values. A generator function returns a generator object,
which can be used to generate the values one-by-one as you iterate over it. 
Generators are a powerful tool for working with large or complex data sets, as
they allow you to generate the values on-the-fly, rather than having to create
and store the entire sequence in memory.

Creating a Generator

In Python, you can create a generator by using the yield statement in a
function. The yield statement returns a value from the generator and suspends
the execution of the function until the next value is requested. Here's an 
example:
'''

def generator():
  for i in range(5):
    yield i

gen = generator()

#* the "next" method gets the next value from the generator
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
# print(next(gen)) #! reach its end through error
