'''
The time Module in Python

The time module in Python provides a set of functions to work with time-related
operations, such as timekeeping, formatting, and time conversions. This module
is part of the Python Standard Library and is available in all Python 
installations, making it a convenient and essential tool for a wide range 
of applications.
'''

import time

#*Print time in seconds
print("Time in Seconds: ", time.time())

#* Print time in after 3 seconds
time.sleep(3)
print("I'm Printing After 3 Seconds!")

#* The time.strftime() function formats a time value as a string, based on a specified format.
t = time.localtime()
formatted_time = time.strftime("%Y:%m:%d %H:%M:%S", t)
print("The formatted time: ",formatted_time)