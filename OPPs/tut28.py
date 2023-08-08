'''
Exercise 11 - Drink Water Reminder

Write a python program which reminds you of drinking water every hour or two.
Your program can either beep or send desktop notifications for a specific 
operating system
'''

from plyer import notification
import time
import os

# Ask the user for reminder time in minutes
reminder_time = int(input("How many minutes between reminders? "))

# Use while loop to create notifications indefinitely
while True:
    # Notification
    notification.notify(
        title="Reminder to take a break",
        message="Drink water, take a walk",
        timeout=10  # Display the notification for 10 seconds
    )

    # System pause the execution of this program for the specified reminder_time
    time.sleep(reminder_time * 60)  # Convert minutes to seconds

    # Clear the terminal screen (works on most systems, but not all)
    os.system('clear')  # For Linux/Mac
    os.system('cls')    # For Windows



