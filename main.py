from library_books import library_books
from datetime import date, datetime, timedelta
import string
import copy
import time

#references used:
#https://www.w3schools.com/python/python_dictionaries_copy.asp
#https://www.w3schools.com/python/python_datetime.asp

class Book:

    def __init__(self, library_books):
        self.library_books = library_books

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

    def viewAllBooks(self):
        print("Here are all of the books in the library: \n")
        time.sleep(1)
        for book in self.library_books:
            if book.get("available") == True:
                print(f"Book ID: {book.get("id")} - {book.get("title")} by {book.get("author")}")

    #TEST: viewAllBooks(library_books)



    # -------- Level 2 --------
    # TODO: Create a function to search books by author OR genre
    # Search should be case-insensitive
    # Return a list of matching books

    #Understand: I have to create a function where the user can search library_books by either author or genre
    # - Inputs = string stating author or genre; Outputs list of books with that author or genre; Edge cases is if the book is not found in library books
    #Clues: As it involves searching, I will need to use for loops. I might also need to use string methods to make it case sensitive.
    #Assemble:

    #DEFINE function bookSearch - input String searchValue
        #author_list created with values of authors from library_books
        #genre_list created with values of genres from library_books
        #IF searchValue in author_list
            #print "Books by author searchValue"
        #ELSE IF searchValue in genre_list
            #print "Books in genre searchValue"
        #ELSE
            #PRINT "Book is not found in library"
        #FOR each book in library_books
            #IF book author equals searchValue or book genre equals searchValue
                #print book

    def bookSearch(self, searchValue):
        author_list = [book.get("author") for book in self.library_books]
        genre_list = [book.get("genre") for book in self.library_books]
        if any(author.casefold() == searchValue.casefold() for author in author_list):
            print("Here are books by author " + string.capwords(searchValue) + ":")
        elif any(genre.casefold() == searchValue.casefold() for genre in genre_list):
            print("Here are books in the " + string.capwords(searchValue) + " genre:")
        else:
            print("There is no book with this information in this library.")
        time.sleep(1)
        for book in self.library_books:
            if book.get("author").casefold() == searchValue.casefold() or book.get("genre").casefold() == searchValue.casefold():
                print(f"Book ID: {book.get("id")} - {book.get("title")} by {book.get("author")} - Genre: {book.get("genre")} - Is it Available? {book.get("available")} - Due Date: {book.get("due date")} - Number of Checkouts: {book.get("checkouts")}")

    '''TEST:
    bookSearch("fantasy")
    bookSearch("ray bradbury")
    '''
    


    # -------- Level 3 --------
    # TODO: Create a function to checkout a book by ID
    # If the book is available:
    #   - Mark it unavailable
    #   - Set the due_date to 2 weeks from today
    #   - Increment the checkouts counter
    # If it is not available:
    #   - Print a message saying it's already checked out

    #Understand: I have to create a function where the user can check a book based on its ID
    # - Inputs = string stating book ID; Outputs either that you checked out the book or you can't as it is already checked out; edge cases include if the ID is invalid/doesn't match any book
    #Clues: Since I will need search through the library books list, I will need to use for loops. I might also need to use string methods to make my searches case sensitive.
    #Assemble:

    #DEFINE function checkout - input String ID
        #IF ID exists in library
            #FOR each book in library_books
                #IF book ID equals ID
                    #PRINT "Book to checkout: book"
                    #IF book is available
                        #available is set to FALSE
                        #IF due date is currently none
                            #set due date to today's date plus two weeks
                        #ELSE IF due date has a value
                            #due date is date plus two weeks
                        #checkouts equals checkouts plus one
                    #ELSE if book is not available
                        #PRINT "The book is already checked out"
        #ELSE if ID does not exist library
            #PRINT "There is no book in the library with that ID."

    def checkout(self, ID):
        if any(book.get("id").casefold() == ID.casefold() for book in self.library_books):
            for book in self.library_books:
                if book.get("id").casefold() == ID.casefold():
                    print(f"Book to checkout: {book.get("title")} by {book.get("author")}")
                    time.sleep(1)
                    if book.get("available") == True:
                        book["available"] = False
                        if(book.get("due_date") == None):
                            book["due_date"] = str(datetime.now().date() + timedelta(weeks=2))
                        else:
                            print(f"The old due date of {book.get("title")} by {book.get("author")} is {book.get("due_date")} \n")
                            book["due_date"] = str(datetime.strptime(book["due_date"], "%Y-%m-%d").date() + timedelta(weeks=2))
                            time.sleep(1)
                        book["checkouts"] = book["checkouts"] + 1
                        print(f"You just checked out {book.get("title")} by {book.get("author")} - ID: {book.get("id")} - Due Date: {book.get("due_date")} - Number of Checkouts: {book.get("checkouts")} - Currently Available: {book.get("available")}")
                    else:
                        print(f"{book.get("title")} by {book.get("author")} - ID {ID} is already checked out.")
        else:
            print(f"Sorry, there is no book in the library with the book ID {ID}.")

    
    '''
    TEST:
    checkout("B3")
    checkout("B2")
    checkout("B4")
    checkout("C4")
    '''








    # -------- Level 4 --------
    # TODO: Create a function to return a book by ID
    # Set its availability to True and clear the due_date

    ##Understand: I have to create a function where the user can return a book
    # - Inputs = string stating book ID; Output is that you successfully returned a book; edge cases include if the ID is invalid/doesn't match any book
    #Clues: Since I will need search through the library books list to match the IDs, I will need to use for loops. I might also need to use string methods to make my searches case sensitive.
    #Assemble:

    def returnBook(self, bookID):
        if any(book.get("id").casefold() == bookID.casefold() for book in self.library_books):
            for book in self.library_books:
                if book.get("id").casefold() == bookID.casefold():
                    if book.get("available") == False:
                        book["available"] = True
                    if book.get("due_date") != None:
                        book["due_date"] == None
                    availability = "available" if book.get("available") else "not available"
                    time.sleep(1)
                    print(f"{book.get("title")} by {book.get("author")} - {book.get("id")} is now returned and is {availability} for checkout.")
        else:
            print(f"Sorry, there is no book in the library with the book ID {bookID}.")
    #TEST: returnBook("B4")

    # TODO: Create a function to list all overdue books
    # A book is overdue if its due_date is before today AND it is still checked out

    #Understand: I have to create a function that checks which books are overdue and shows them
    # - Inputs = list/dictionary with books; Output is each book that is overdue being printed out; edge cases are if there are no overdue books
    #Clues: Since I will need search through the library books list to check if each book is overdue, I will need to use for loops. I might also need to use string methods to make my searches case sensitive.
    #Assemble:

    def overdueBooks(self):
        print("Here is a list of Overdue Books in the Library: ")
        time.sleep(1)
        for book in self.library_books:
            if book["available"] == False and datetime.strptime(book["due_date"], "%Y-%m-%d").date() < date.today():
                print(f"{book.get("title")} by {book.get("author")} - {book.get("id")}")
    #TEST: overdueBooks(library_books)



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

    def three_most_checked_out(self):
        print("The three most checked out books in the library are: ")
        library_books_duplicate = copy.deepcopy(self.library_books)
        checkout_books = []
        i = 0
        while(len(checkout_books) < 3):
            most_checkouts = library_books_duplicate[0]["checkouts"]
            book_to_add = library_books_duplicate[0]
            for book in library_books_duplicate:
                if book["checkouts"] >= most_checkouts:
                    book_to_add = book
                    most_checkouts = book["checkouts"]
            checkout_books.append(book_to_add)
            for book in library_books_duplicate:
                if book == checkout_books[i]:
                    library_books_duplicate.remove(book)
            i = i + 1
        place = 0
        time.sleep(1)
        for book in checkout_books:
            print(f"{place}. {book.get("title")} by {book.get("author")} - {book.get("id")} - {book.get("checkouts")}")
            place = place + 1

    def add_book(self):
        id_last_num = int(self.library_books[-1].get("id")[-1]) + 1
        id = self.library_books[-1].get("id")[0] + "" + str(id_last_num)
        title = input("Enter the title of the book you want to add: ")
        author = input("Enter the author of the book you want to add: ")
        genre = input("Enter the genre of the book you want to add: ")
        self.library_books.append({"id":id,"title" : title, "author":author, "genre": genre,"available": True, "due_date": None, "checkouts": 0})
        time.sleep(1)
        print(f"You just added the book {self.library_books[-1].get("title")} by {self.library_books[-1].get("author")} (ID: {self.library_books[-1].get("id")}; Genre: {self.library_books[-1].get("genre")}) to the library!")
                




    def menu(self):
        option = int(input("Choose the number for one of the following options: \n 1. View Available Books \n 2. Search By Author or Genre \n 3. Checkout a Book \n 4. Return a Book \n 5. View Overdue Books \n 6. View Top 3 Most Checked-Out Books \n 7. Add A Book to Library \nEnter option: "))
        time.sleep(1)
        if option == 1:
            self.viewAllBooks()
        elif option == 2:
            searchValue = input("Enter either an author or genre to search for books: ")
            self.bookSearch(searchValue)
        elif option == 3:
            bookID = input("Enter the ID of the book you want to check out: ")
            self.checkout(bookID)
        elif option == 4:
            bookID = input("Enter the ID of the book you want to return: ")
            self.returnBook(bookID)
        elif option == 5:
            self.overdueBooks()
        elif option == 6:
            self.three_most_checked_out()
        elif option == 7:
            self.add_book()
        else:
            print("Choose an actual option from the list. ")
            time.sleep(1)
            self.menu()

            

if __name__ == "__main__":
    # You can use this space to test your functions
    my_library = Book(library_books)
    print("Welcome to the library! Choose from the menu to explore our options! \n")
    time.sleep(0.5)
    continue_menu = 1
    while(continue_menu != 2):
        my_library.menu()
        print("\n")
        time.sleep(1)
        continue_menu = int(input("Type 1 for True and 2 for False based on if you want to choose another option from the menu: "))
        time.sleep(1)
    print("Thanks for visiting the library!")
    
