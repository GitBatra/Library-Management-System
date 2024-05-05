class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class BookManager:
    def __init__(self, books=None):
        self.books = books if books else []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

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
