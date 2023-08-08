'''
How importing in python works

Importing in Python is the process of loading code from a Python module into the current script. 
This allows you to use the functions and variables defined in the module in your current script, 
as well as any additional modules that the imported module may depend on.
'''

# import specific methods
from math import sqrt, pi
print(sqrt(2), pi) #1.4142135623730951 3.141592653589793

# also use as keyword argument
from math import sqrt as sq, pi

print(sq(20)) #4.47213595499958

# Also change the whole name of library
import math as math_python

print(math_python.sqrt(20)) #4.47213595499958

# Also print whole methods of lib using "dir" method
print(dir(math_python))
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''

# Also make custom file and import methods from him
from haseeb import haseeb as hb, welcome

# Methods from another files
print(hb)
welcome()

