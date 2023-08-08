'''
if "__name__ == "__main__" in Python
The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

Here's an example of how the if __name__ == __main__ idiom can be used:
'''

from haseeb import welcome, haseeb as hb 
# ! By simply importing this module if there is anything executable in file "haseeb.py" it automatically executes
#? so be careful while importing
#* to overcome this problem we use the "if __name__ == __main__" function in that file

# Now print the "Welcome Haseeb Khan!" only one time
welcome() 