'''
Docstrings in python

Python docstrings are the string literals that appear right after the definition of a function, 
method, class, or module.
'''

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
  
print(add(10,20).__doc__) #Prints the documentation of the add method


'''
PEP 8
PEP 8 is a document that provides guidelines and best practices on how to write Python code. 
It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. 
A PEP is a document that describes new features proposed for 
Python and documents aspects of Python, like design and style, for the community.
'''