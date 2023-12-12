import datetime


class Book:
    def __init__(self, title, description, image=None) -> None:
        self.title = title
        self.description = description
        self.image = image
        self.available = True
        self.borrower = None
        self.due_date = None

    def borrow(self, borrower, length):
        self.available = False
        self.borrower = borrower
        self.due_date = datetime.date.today() + datetime.deltatime(days=length)

    def return_book(self):
        self.available = True
        self.borrower = None
        self.due_date = None

    def get_basic_details(self):
        return [self.title, self.description, self.image, self.available]

    def get_full_details(self):
        return [
            self.title,
            self.description,
            self.image,
            self.available,
            self.due_date,
            self.borrower,
        ]
