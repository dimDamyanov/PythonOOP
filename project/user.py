from project.library import Library


class User:
    books = []

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if author in Library.books_available and book_name in Library.books_available[author]:
            User.books.append(book_name)
            Library.books_available[author].remove(book_name)
            Library.rented_books[self.username][book_name] = days_to_return
            return f'{book_name} successfully rented for the next {days_to_return} days!'
        else:
            raw_rented_books_data = [book_data.items() for book_data in Library.rented_books.values()]
            rented_books_data = [y for x in raw_rented_books_data for y in x]
            for search_book_name, search_days_to_return in rented_books_data:
                if search_book_name == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {search_days_to_return} days!'
        return

    def re
