from users import User
from books import Book
import datetime


class ViableLibrary:
    """Create a blank instance of ViableLibrary."""

    def __init__(self) -> None:
        self.books = {}  # title as key
        self.users = {}  # email as key
        self.current_user = None
        self.borrow_time = 21

    def register(self, first_name, last_name, email, password) -> bool:
        """Register a new user and return a bool."""
        if email not in self.users:
            self.users[email] = User(first_name, last_name, email, password)
            return True
        else:
            return False

    def login(self, email, password):
        """Check if email and password is a valid combination and return bool."""
        self.logout()
        if email in self.users and self.users[email].login(password):
            self.current_user = self.users[email]
            return True
        return False

    def logout(self):
        """Clear current user and return bool."""
        if self.current_user:
            self.current_user.logout()
        self.current_user = None
        return True

    def borrow(self, title):
        """Check out book and return due date if successful, False otherwise."""
        if self.current_user and self.books[title].available:
            self.books[title].borrow(self.current_user.email, self.borrow_time)
            return self.books[
                title
            ].due_date  # currently this returns either a date or a bool
        return False  # while a date will evaluate to True, this is not very clean.
        # Potentially refactor all False returns to exceptions

    def return_book(self, title):
        """Mark book as not on loan and return bool."""
        if self.current_user and not self.books[title].available:
            self.books[title].return_book()
            return True
        return False

    def get_book_list(self):
        """Return the list of books."""
        return [self.books[title].get_basic_details() for title in self.books]

    def get_available_books(self):
        """Return the list of books avaiable for borrowing."""
        return [
            self.books[title].get_basic_details()
            for title in self.books
            if self.books[title].available
        ]

    def get_due_books(self):
        """Return the list of books due back today."""
        return [
            self.books[title].get_basic_details()
            for title in self.books
            if self.books[title].due_date == datetime.date.today()
        ]

    def get_loaned_books(self):
        """Return the list of books currently on loan with borrower details."""
        withoutNames = [
            self.books[title].get_full_details()
            for title in self.books
            if not self.books[title].available
        ]
        return [
            book + self.users[book[-1]].get_names() for book in withoutNames
        ]  # Here we need to add additional information about the borrower

    def add_book(self, title, description, image=None):
        """Add a book to the library dataset and return bool"""
        if title not in self.books:
            self.books[title] = Book(title, description, image)
            return True
        return False
