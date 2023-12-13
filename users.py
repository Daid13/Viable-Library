class User:
    def __init__(self, first_name, last_name, email, password):
        """Create a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._password = password  # not secure enough but ran out of time to research cryptographic hash libraries
        self.logged_in = False

    def login(self, password):
        """Compare entered password to actual and return bool."""
        if self._password == password:
            self.logged_in = True
            return True
        else:
            return False

    def logout(self):
        """Mark as logged out"""
        self.logged_in = False

    def get_names(self):
        """Return user's first name and last name as a list."""
        return [self.first_name, self.last_name]
