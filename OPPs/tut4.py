'''
Getters

Getters in Python are methods that are used to access the values of an 
object's properties. They are used to return the value of a specific property, 
and are typically defined using the @property decorator. 

Setters

It is important to note that the getters do not take any parameters and we 
cannot set the value through getter method.For that we need setter 
method which can be added by decorating method with @property_name.setter
'''

#? getter & setter methods is nothing but a way in which a method is act like a variable or property
# Here is an example of a simple class with a getter method:
# to get we use @property
# to set we use @value_name.setter
class MyClass:
  def __init__(self, value):
    self._value = value
  def show(self):
    print(f"Value is {self._value}")
  @property
  def ten_value(self):
    return 10 * self._value
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10
  
obj = MyClass(10)
obj.show()

obj1 = MyClass(20)
print(obj1.ten_value)
obj1.ten_value = 300
print(obj1.ten_value)
obj.show()