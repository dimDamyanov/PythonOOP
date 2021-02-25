class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user):
        if user not in self.user_records:
            return 'We could not find such user to remove!'
        else:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        for i in range(len(self.user_records)):
            if self.user_records[i].user_id == user_id:
                if self.user_records[i].username == new_username:
                    return 'Please check again the provided username - it should be different than the username used so far!'
                else:
                    if self.user_records[i].username in self.rented_books:
                        self.rented_books[new_username] = self.rented_books[self.user_records[i].username]
                        del self.rented_books[self.user_records[i].username]
                    self.user_records[i].username = new_username
                    return f'Username successfully changed to: {new_username} for userid: {user_id}'
        return f'There is no user with id = {user_id}!'
