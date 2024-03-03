class Book:
    def __init__(self, author, publisher, title, genre):
        self.author = author
        self.publisher = publisher
        self.title = title
        self.genre = genre
        self.borrowed_status = "FALSE"
        self.date_borrowed = ""
        self.total_times_borrowed = 0

class AddOrRemoveBooks:
    # contains methods to add and remove books
    def __init__(self):
        pass
    def removeBook(self, book: Book):
        # this would make a connection to a database, search for the book name, then remove it
        if (True):
            print(f"{book.title} has been removed from the catalog!")   
        else:
            print(f"Unable to find {book.title} in catalog.")
    
    def addBook(self, book: Book):
        # this would make a connection to a database, then add the book + its details to the database, would check if it already exists
        # if (True): (book exists)
        #     print(f"Book is already in the catalog.")
        # add the book
        print(f"{book.title} has been added to the catalog!")
    
class Search:
    # all of these would use the database to search for the attribute passed into their method
    def __init__(self):
        pass
    def searchByAuthor(self, author):
        # would search "library" db for the author, and return all books by them, if none exist print("no books found")
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        print(f"These are all the books by {author}: ")
        for book in mockLibrary:
            if (book.author == author):
                print(book.title)
        

    def searchByTitle(self, title):
        # would search "library" db for title and return the book with its info, if none exist print("no books found")
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        print("Here is the book found: ")
        for book in mockLibrary:
            if (book.title == title):
                print(book.title)
        

    def searchByGenre(self, genre):
        # would search "library" db for the genre, return all books with this genre, if none exist print("no books found")
        # ex// query = "SELECT title from library WHERE borrowed_status = 'genre'"
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        print(f"Here are all the books with genre {genre}: ")
        for book in mockLibrary:
            if (book.genre == genre):
                print(book.title)

class BorrowAndReturn:
    def __init__(self):
        pass
    def borrowBook(self, title):
        # this would search the database using book.title, check if column "borrowed_status" == "TRUE" for the book, if not, allow the book to be borrowed
        # then change the table column "borrowed_status" to TRUE, change "date_borrowed" to the current date, and increment "total_times_borrowed"
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        for book in mockLibrary:
            if (title == book.title):
                if (book.borrowed_status != "TRUE"):
                    book.borrowed_status = "TRUE"
                    book.date_borrowed = "3/1/24"
                    book.total_times_borrowed = book.total_times_borrowed + 1
                    print(f"You have succesfully borrowed {book.title}. Please return it within 14 days.")
                else:
                    print(f"{book.title} is already borrowed.")

    def returnBook(self, title):
        # use book.title to check if "borrowed_status" =="TRUE" in the database, if FALSE: print("{book.title} is not borrowed")
        # if TRUE: change "borrowed_status" to "FALSE" and then clear the "date_borrowed" colunn for this book
        # since this array is not global it will always return not borrowed, but it is just an example
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        for book in mockLibrary:
            if (title == book.title):
                if (book.borrowed_status == "TRUE"):
                    book.borrowed_status = "FALSE"
                    book.date_borrowed = ""
                    print(f"You have succesfully returned {book.title}.")
                else:
                    print(f"{book.title} is not borrowed.")

class Reports:
    def __init__(self):
        pass
    def borrowedReport(self):
        # this would search the database for every single book with "borrowed_status" == TRUE, and return a list of them
        # ex// query = "SELECT title from library WHERE borrowed_status = 'TRUE'"
        book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
        mockLibrary = [book1]
        print("Here are all the books that are borrowed: ")
        for book in mockLibrary:
            if(book.borrowed_status == "TRUE"):
                print(book.title)

    def overdueReport(self):
        # overdueReport would compare the timeDelta from the current date to the date borrowed. returns a list of each book > 14 days overdue
        print(f"Book is overdue.")

    def popularityReport(self, book: Book):
        # this would search the database for the book passed in using book.title and check the "total_times_borrowed" attribute
        # ex// query = "SELECT total_times_borrowed from library where title = %s" (then set a var = book.title and execute)
        # when executed, return the value and place it in a var, popularity.
        # ex// popularity is 54 (total_times_borrowed = 54)
        popularity = 54
        if (popularity >= 100):
            print(f"{book.title} is extremely popular!")
        elif ((popularity >= 50) and (popularity < 100)):
            print(f"{book.title} is popular!")
        elif ((popularity >= 25) and (popularity < 50)):
            print(f"{book.title} is somewhat popular.")
        else:
            print(f"{book.title} is not very popular...")


# each type of user inherits the classes with the methods that they are allowed to use; guest can search. user can search, borrow, return.
# librarian can get reports, and add or remove books from the library/catalog
class Guest(Search):
    def __init__(self):
        pass

class User(Search, BorrowAndReturn):
    def __init__(self, username):
        self.name = username

class Librarian(Reports, AddOrRemoveBooks):
    def __init__(self):
        pass

def main():
    book1 = Book("Suzanne Collins", "Scholastic", "The Hunger Games", "Dystopian")
    mockLibrary = [book1]

    guest1 = Guest()

    guest1.searchByAuthor("Suzanne Collins")
    guest1.searchByGenre("Dystopian")
    guest1.searchByTitle("The Hunger Games")

    user1 = User("khaz")

    user1.searchByAuthor("Suzanne Collins")
    user1.borrowBook("The Hunger Games")

    headLibrarian = Librarian()

    headLibrarian.popularityReport(book1)

if __name__ == "__main__":
    main()