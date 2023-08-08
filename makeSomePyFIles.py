import os

#* Generate file
# Generate Sub folders as well
for index,i in enumerate(range(0, 20)):
  with open(f'OPPs/tut{index+20}.py', 'w') as file:
    file.write("'''\n'''")