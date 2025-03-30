import json

class MyLibrary:

    #---==== INITIALIAZES A NEW MYLIBRARY OBJECT ====--#
    def __init__(self): # __init__ is a constructor and it is automatically called when an instance of the class is created.
        #--==== When the values do not depend on user input, they don’t need to be passed as parameters. ====--#
        #--==== They can still be accessible using self.books and self.booksFile because self refers to the current instance. ====--#
        self.books = [] # Initializes an empty list that will hold book records
        self.booksFile = 'library.json'  # Specifies the file where books will be stored
        self.loadBooks() # Calls a method to load books from the file


    #--==== FUNCTION TO LOAD BOOKS FROM A FILE ====--#
    def loadBooks(self):
        try:
            # with statement ensures that resources are properly closed or released, even if an error occurs during execution.
            with open(self.booksFile, 'r') as f: # Opens 'library.json' in read mode / Python provides different file modes so 'r' is a Read mode (default).
                self.books = json.load(f) # Loads book data from JSON file into self.books
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = [] # If file not found or corrupt, initialize an empty list


    #--==== FUNCTION TO LOAD BOOKS FROM A FILE ====--#
    def saveBooks(self):
        """Save the library to a file."""
        with open(self.booksFile, "w") as file: # The "w" mode (write mode) means it will overwrite the file if it already exists or create a new one if it doesn’t.
            json.dump(self.books, file, indent=4) # json.dump() converts self.books (which is likely a dictionary or list) into a JSON-formatted string and writes it to the file.
                                                  # indent=4 ensures that the JSON file is formatted with 4 spaces per indentation level, making it more readable.  

    #--==== FUNCTION TO ADD BOOKS ====--#
    def addBooks(self):
        # this will take inputs of details of book
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter publication year: ")
        genre = input("Enter genre: ")
        read_status = input("Have you read it? (yes/no): ").strip().lower()
        
        # a dictionary where values of key are taken from above variables
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status == "yes" # This checks if read_status is "yes". If read_status == "yes" then "read" is set to True otherwise "read" is set to False.
        }
        self.books.append(book) # this will add the book to books
        self.saveBooks() # this will save the updates in to the file
        print(f"Book '{title}' added successfully!\n")

    #--==== FUNCTION TO REMOVE BOOKS ====--#
    def removeBooks(self):
        title = input("Enter the title of the book to remove: ") # input for the name of book to be removed
        for book in self.books: # this will loop through the books
            if book["title"].lower() == title.lower(): # this will match the input with books
                self.books.remove(book) # this will remove the book if it will get matched with the input
                self.saveBooks() # this will save the updates in to the file
                print(f"Book '{title}' removed successfully!\n")
                return
        print("Book not found!\n") # if the input does not match any of the books' title then this message will be shown

    #--==== FUNCTION TO SEARCH BOOKS ====--#
    def searchBooks(self):
        searchTerm = input("Enter a title or author to search: ").lower() # input for the book to be searched
        results = [
            book
            for book in self.books # it will loop through all the books
            if searchTerm in book["title"].lower() # this will see if the searchTerm matches any title
            or searchTerm in book["author"].lower() # or if the searchTerm matches any author
        ] 
        if results: # if the searchTerm matches the book
            for book in results: # this will loop through the matching books
                self.displayBook(book) # and then this will call the functiom and prints the book
        else:
            print("No matching books found.\n") # if the searchTerm does not match then this message will be shown

    def displayBook(self, book): # function to display details of searched book
        status = "Read" if book["read"] else "Not Read"  # this will check the book["read"] value if itis True then status will be "read" if it is False then status will be "Not Read"
        print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nStatus: {status}\n") # printing details | \n creates a new line

    #--==== FUNCTION TO DISPLAY ALL BOOKS ====--#
    def viewBooks(self):
        if not self.books:
            print("No books in the library.\n")
            return
        for book in self.books:
            self.displayBook(book)

    #--==== FUNCTION TO DISPLAY STATISTICS ====--#
    def statistics(self):
        total_books = len(self.books) # this will return the total number of books.
        read_books = sum(1 for book in self.books if book["read"]) # this wll loop through each book in self.books If book["read"] is True it adds 1 to the sum. The result will be the total count of read books.
        unread_books = total_books - read_books # calculates unread books by subtracting read books from total books.
        print(f"\nTotal books: {total_books}\nRead books: {read_books}\nUnread books: {unread_books}\n") # this will print total books, read books and unread books

    #--==== FUNCTION TO DISPLAY OPTIONS FOR USER ====--#
    def options(self):
        while True: # throught while loop the following options will be printed
            print("\n 📔 Welcome To Personal Library Manager 📔")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. View all books")
            print("5. View statistics")
            print("6. Exit")
            choice = input("Enter your choice (1 to 6): ") # variable for user to enter option of their choice

            if choice == "1": # if else condition to execute a function based on user choice
                self.addBooks()
            elif choice == "2":
                self.removeBooks()
            elif choice == "3":
                self.searchBooks()
            elif choice == "4":
                self.viewBooks()
            elif choice == "5":
                self.statistics()
            elif choice == "6":
                print("Exiting...\n")
                break
            else:
                print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    LibraryManager = MyLibrary()
    LibraryManager.options()