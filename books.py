import datetime


class Book:
    def __init__(self, title, description, image=None) -> None:
        """Create an instance of book and mark as available."""
        self.title = title
        self.description = description
        self.image = image
        self.available = True
        self.borrower_email = None
        self.due_date = None

    def borrow(self, borrower, length):
        """Set book as on loan."""
        self.available = False
        self.borrower_email = borrower
        self.due_date = datetime.date.today() + datetime.timedelta(days=length)

    def return_book(self):
        """Set book to available to borrow."""
        self.available = True
        self.borrower_email = None
        self.due_date = None

    def get_basic_details(self):
        """Return book details and availablity."""
        return [self.title, self.description, self.image, self.available]

    def get_full_details(self):
        """Return book details and borrower information."""
        return [
            self.title,
            self.description,
            self.image,
            self.available,
            self.due_date,
            self.borrower_email,
        ]
