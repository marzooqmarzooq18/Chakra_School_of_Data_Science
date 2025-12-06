# -------------------- Class: Book --------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_available = True  # private attribute

    def mark_borrowed(self):
        """Mark the book as borrowed."""
        self.__is_available = False

    def mark_returned(self):
        """Mark the book as returned (available again)."""
        self.__is_available = True

    def is_available(self):
        """Return True if book is available."""
        return self.__is_available

    def show_info(self):
        """Display book details and current availability."""
        status = "Available" if self.__is_available else "Issued"
        print(f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")


# -------------------- Class: Member --------------------
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.__borrowed_books = []  # private list

    def borrow_book(self, book):
        """Borrow a book if available."""
        if book.is_available():
            book.mark_borrowed()
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed \"{book.title}\"")
        else:
            print(f"{self.name} tried to borrow \"{book.title}\" → Book already issued.")

    def return_book(self, book):
        """Return a borrowed book."""
        if book in self.__borrowed_books:
            book.mark_returned()
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned \"{book.title}\"")
        else:
            print(f"{self.name} didn’t borrow \"{book.title}\"")

    def show_borrowed_books(self):
        """Show all currently borrowed book titles."""
        titles = [book.title for book in self.__borrowed_books]
        print(f"{self.name}’s Borrowed Books: {titles}")


# -------------------- Class: Library --------------------
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        self.members = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)
        print(f"Book Added: {book.title}")

    def add_member(self, member):
        """Add a library member."""
        self.members.append(member)
        print(f"Member Added: {member.name}")

    def show_all_books(self):
        """Display all books with their details."""
        print(f"\nAll Books in {self.library_name}:")
        for book in self.books:
            book.show_info()

    def show_available_books(self):
        """Show only available books."""
        print("\nAvailable Books:")
        available = [book.title for book in self.books if book.is_available()]
        if available:
            for title in available:
                print(f"- {title}")
        else:
            print("No books available.")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create Library
    library = Library("Chakra Central Library")

    # Create Books
    b1 = Book(101, "Python for Data Science", "Jake VanderPlas")
    b2 = Book(102, "Machine Learning 101", "Andrew Ng")
    b3 = Book(103, "Deep Learning Made Easy", "Ian Goodfellow")
    b4 = Book(104, "AI for Everyone", "Geoffrey Hinton")

    # Add Books
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)

    # Create Members
    m1 = Member(201, "Arjun")
    m2 = Member(202, "Meena")
