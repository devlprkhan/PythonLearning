'''
readlines() method

The readline() method reads a single line from the file. 
If we want to read multiple lines, we can use a loop.


writelines() method

The writelines() method in Python writes a sequence of strings to a file. 
The sequence can be any iterable object, such as a list or a tuple.
'''

#* readlines() line by line
file = open("my2.txt", 'r')
while True:
  line = file.readline()
  if not line:
    break
  print(line)
file.close()

#* writelines()
file = open("my3.txt", 'w') #create a new file if not exists
lines = ['line 1\n', 'line 2\n', 'line 3\n']
file.writelines(lines)
file.close()

f = open('my2.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)