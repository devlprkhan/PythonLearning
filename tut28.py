'''
Raising Custom errors
In python, we can raise custom errors by using the raise keyword.
'''
salary = input("Enter salary amount: ")
if salary == 'quit':
  print("Quitting the program!")
elif not int(salary) < 2000 < int(salary) < 5000:
  raise ValueError("Salary should be between 2000 and 5000")