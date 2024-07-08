from exceptions import UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists("Username already exists")
        if len(password) < 8:
            raise PasswordTooShort("Password must be at least 8 characters long")
        self.users[username] = User(username, password)

    def login(self, username, password):
        if username not in self.users:
            raise InvalidUsername("Invalid username")
        try:
            return self.users[username].login(password)
        except InvalidPassword:
            raise InvalidPassword("Invalid password")

    def is_logged_in(self, username):
        return self.users.get(username, None).is_logged_in if username in self.users else False
