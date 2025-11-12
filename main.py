from library_books import library_books
from datetime import datetime, timedelta
import string

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

#Understand: I need to print out the books in library_books.py, making sure to show book ID, title, and author
# - Input is going to be a list (which is library_books), and output is going to be a String of all the books and their info; edge cases are if library_books list doesn't have all the info/blank info
#Clues: I likely will need to use a for loop as I'm going to traverse through all of library_books.py. I will also have to use string methods and fstrings as I'm printing it out.
#Assemble:

#FUNCTION viewAllBooks (input library_books)
    #Print "Here are all of the books in the library: " + new line
    #FOR each book in library_books
        #IF Available is equal to true THEN
            #print book ID + title + authore 

def viewAllBooks(library_books):
    print("Here are all of the books in the library: \n")
    for book in library_books:
        if book.get("available") == True:
            print(f"Book ID: {book.get("id")} - {book.get("title")} by {book.get("author")}")

viewAllBooks(library_books)



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

#Understand: I have to create a function where the user can search library_books by either author or genre
# - Inputs = string stating author or genre; Outputs list of books with that author or genre
#Clues: As it involves searching, I will need to use for loops. I might also need to use string methods to make it case sensitive.
#Assemble:

#DEFINE function bookSearch - input String searchValue
    #author_list created with values of authors from library_books
    #genre_list created with values of genres from library_books
    #IF searchValue in author_list
        #print "Books by author searchValue"
    #ELSE IF searchValue in genre_list
        #print "Books in genre searchValue"
    #FOR each book in library_books
        #IF book author equals searchValue or book genre equals searchValue
            #print book

def bookSearch(searchValue):
    author_list = [book.get("author") for book in library_books]
    genre_list = [book.get("genre") for book in library_books]
    if any(author.casefold() == searchValue.casefold() for author in author_list):
        print("Here are books by author " + string.capwords(searchValue) + ":")
    elif any(genre.casefold() == searchValue.casefold() for genre in genre_list):
        print("Here are books in the " + string.capwords(searchValue) + " genre:")
    for book in library_books:
        if book.get("author").casefold() == searchValue or book.get("genre").casefold() == searchValue:
            print(f"Book ID: {book.get("id")} - {book.get("title")} by {book.get("author")} - Genre: {book.get("genre")} - Is it Available? {book.get("available")} - Due Date: {book.get("due date")} - Number of Checkouts: {book.get("checkouts")}")

bookSearch("fantasy")
bookSearch("ray bradbury")


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
