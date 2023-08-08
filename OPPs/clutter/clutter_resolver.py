'''
Exercise # 7

Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the 
way till n.png where n is the number of png files in that folder. 
Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png
'''

# Solution

import os

def fileRename(file, index):
  file_path, file_extension = os.path.splitext(file)
  new_file_name = str(index) + file_extension
  new_file_path = os.path.join("./OPPs/clutter/", new_file_name)
  os.rename(f"./OPPs/clutter/{file}", new_file_path)


files = os.listdir("./OPPs/clutter/")
for index, file in enumerate(files):
  if not file.endswith('.py'):
    fileRename(file, index+1)
  
