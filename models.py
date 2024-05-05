class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class CheckOut:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
