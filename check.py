class CheckOut:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

class CheckOutManager:
    def __init__(self):
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        self.checkouts.append(CheckOut(user_id, isbn))
