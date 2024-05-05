class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self, users=None):
        self.users = users if users else []

    def add_user(self, name, user_id):
        self.users.append(User(name, user_id))

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")

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
