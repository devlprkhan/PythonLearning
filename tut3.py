'''
Two Types of Typecasting:
Explicit Conversion (Explicit type casting in python)
Implicit Conversion (Implicit type casting in python).
'''
print("===============TYPE Casting==================")
# Explicit
# Without Type Casting (12)
a='1'
b='2'

print("Without Type Casting: ", a+b)

# With Type Casting (3)
a='1'
b='2'

print("With Type Casting: ", int(a) + int(b))

# Implicit (automatically performed by python)
a=9.9
b=1
print("Implicit Type Casting: ", a+b)
print("=================================")
