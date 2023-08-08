'''
Exercise#9

Write a program to pronounce list of names using win32 API. 
If you are given a list l as follows:

l = ["Rahul", "Nishant", "Harry"]

Your program should pronouce:

Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry
'''

import win32com.client as wincl

shoutOutlist = ['Haseeb', 'Tayyab', 'Mubeen', 'Ameen', 'Mahnoorfatimah']
def pronounce_text(text):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

for member in shoutOutlist:
    pronounce_text(f"Shoutout to {member}")

