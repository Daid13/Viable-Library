import User
import book
import datetime


class Library:
    def __init__(self) -> None:
        self.books = {}  # title as key
        self.users = {}  # email as key
        self.current_user = None
        self.borrow_time = 21

    def register(self, first_name, last_name, email, password):
        if email not in self.users:
            self.users[email] = User(first_name, last_name, email, password)
            return True
        else:
            return False

    def login(self, email, password):
        self.logout()
        if email in self.users and self.users[email].login(password):
            self.current_user = self.users[email]
            return True
        return False

    def logout(self):
        self.current_user.logout()
        self.current_user = None
        return True

    def borrow(self, title):
        if self.current_user and self.books[title].available:
            self.books[title].borrow()
            # update something in current user?
            return self.books[title].due_date
        return False

    def return_book(self, title):
        if self.current_user and not self.books[title].available:
            self.books[title].return_book()
            # update current user?
            return True
        return False

    def get_book_list(self):
        return [self.books[title].get_basic_details() for title in self.books]

    def get_available_books(self):
        return [
            self.books[title].get_basic_details()
            for title in self.books
            if self.books[title].available
        ]

    def get_due_books(self):
        return [
            self.books[title].get_basic_details()
            for title in self.books
            if self.books[title].due_date == datetime.date.today()
        ]

    def get_loaned_books(self):
        temp = [
            self.books.get_full_details()
            for title in self.books
            if not self.books[title].available
        ]
        return [
            book + self.users[book[-1].get_names()] for book in temp
        ]  # refactor. This adds borrower's names
