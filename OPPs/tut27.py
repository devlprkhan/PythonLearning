'''
Function Caching in Python

Function caching is a technique for improving the performance of a program by 
storing the results of a function call so that you can reuse the results 
instead of recomputing them every time the function is called. This can be 
particularly useful when a function is computationally expensive, or when the 
inputs to the function are unlikely to change frequently.

In Python, function caching can be achieved using the functools.lru_cache 
decorator. The functools.lru_cache decorator is used to cache the results of a 
function so that you can reuse the results instead of recomputing them every 
time the function is called. Here's an example:
'''

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def take_time_print(n):
  time.sleep(5)
  return n*5

print(take_time_print(20))
print("done for 20")
print(take_time_print(10))
print("done for 10")
print(take_time_print(5))
print("done for 5")

#* Executes fast because its cached
print(take_time_print(20))
print("done for 20")
print(take_time_print(10))
print("done for 10")
print(take_time_print(5))
print("done for 5")