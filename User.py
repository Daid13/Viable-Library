class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._password = password
        self.logged_in = False

    def login(self, password):
        if self.password == password:
            self.logged_in = True
            return True
        else:
            return False

    def logout(self):
        self.logged_in = False

    def get_names(self):
        return [self.first_name, self.last_name]
