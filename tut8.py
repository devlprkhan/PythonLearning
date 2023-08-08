import time

print("==================Greeting According to the time Ex#2==================")
'''
Task: Write a Program That is Greeting User According to the time.
'''
# Solution
'''
To provide a more comprehensive breakdown:
Good Morning: Typically used from around 12:00 AM (midnight) until around 11:59 AM.
Good Afternoon: Typically used from around 12:00 PM (noon) until around 5:59 PM.
Good Evening: Typically used from around 6:00 PM until around 11:59 PM (midnight).
'''

current_time = time.localtime()
hour = current_time.tm_hour

if(hour > 12):
  print('Good Morning!')
elif (hour < 18):
  print("Good Afternoon!")
else: 
  print("Good Evening!")
print("==================================================")
