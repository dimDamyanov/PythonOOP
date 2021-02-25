from project.user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user: User):
        if user not in Library.user_records:
            Library.user_records.append(user)
            Library.rented_books[user] = {}
        else:
            return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user: User):
        if user not in Library.user_records:
            return 'We could not find such user to remove!'
        else:
            Library.user_records.remove(user)
            if user.username in Library.rented_books:
                del Library.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        for i in range(len(Library.user_records)):
            if Library.user_records[i].user_id == user_id:
                if Library.user_records[i].username == new_username:
                    return 'Please check again the provided username - it should be different than the username used so far!'
                else:
                    if Library.user_records[i].username in Library.rented_books:
                        Library.rented_books[new_username] = Library.rented_books[Library.user_records[i].username]
                        del Library.rented_books[Library.user_records[i].username]
                    Library.user_records[i].username = new_username
        return 'There is no user with id = {user_id}!'
   