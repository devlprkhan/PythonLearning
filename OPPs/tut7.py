'''
Exercise#6

Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you 
can print all books, add a book and get the number of books using different methods.
Show that your program doesnt persist the books after the program is stopped!
'''

# Solution
class Library:
  def __init__(self):
    self._books = ["English", "Urdu", "SST", "Mathematics"]
    
  def add_book(self, book):
    return self._books.append(book)
  
  def get_no_of_books(self):
    return len(self._books)
  
  def print_all_books(self):
    return self._books
  
library = Library()
user_options=[1,2,3]
user_input = int(input(f"==========Welcome to Library==========\nPlease select a option:\n1:Get a list of books,\n2:Get a number of books,\n3:Add a book,\n\n"))


if (user_input in user_options):
  if (user_input == 1):
    print("\nHere is the list of all books present in library: ",library.print_all_books())
  elif (user_input == 2):
    print("\nThe number of books present in library is: ",library.get_no_of_books())
  elif (user_input == 3):
    user_input_book = input("Enter you book name: ")
    library.add_book(user_input_book)
    print(library.print_all_books())
else:
  raise ValueError("Please Select Valid Options!")