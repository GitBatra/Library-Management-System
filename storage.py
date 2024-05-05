import json

class BookStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_books(self, books):
        with open(self.filename, 'w') as file:
            json.dump([vars(book) for book in books], file)

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Book(**book_data) for book_data in data]
        except FileNotFoundError:
            return []

class UserStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_users(self, users):
        with open(self.filename, 'w') as file:
            json.dump([vars(user) for user in users], file)

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [User(**user_data) for user_data in data]
        except FileNotFoundError:
            return []
