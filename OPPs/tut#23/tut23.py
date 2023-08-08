'''
Shutil Module in Python

Shutil is a Python module that provides a higher level interface for working
with file and directories. The name "shutil" is short for shell utility. It 
provides a convenient and efficient way to automate tasks that are commonly
performed on files and directories. In this repl, we'll take a closer look at 
the shutil module and its various functions and how they can be used in Python.
'''

import shutil

# Copying a file
shutil.copy("./OPPs/tut#23/test.txt", "./OPPs/tut#23/dst.txt")
# Copying a directory
shutil.copytree("./OPPs/tut#23/src_dir", "./OPPs/tut#23/dst_dir")
# Moving a file
shutil.move("./OPPs/tut#23/test.txt", "./OPPs/tut#23/src_dir/dst.txt")
# Deleting a directory
shutil.rmtree("./OPPs/tut#23/dst_dir")