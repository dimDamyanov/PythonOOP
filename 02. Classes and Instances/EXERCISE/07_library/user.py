from .library import Library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if author in library.books_available and book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f'{book_name} successfully rented for the next {days_to_return} days!'
        else:
            raw_rented_books_data = [book_data.items() for book_data in library.rented_books.values()]
            rented_books_data = [y for x in raw_rented_books_data for y in x]
            for search_book_name, search_days_to_return in rented_books_data:
                if search_book_name == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {search_days_to_return} days!'
        return

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name not in self.books:
            return f'{self.username} doesn\'t have this book in his/her records!'
        else:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            del library.rented_books[self.username][book_name]

    def info(self):
        sorted_books = sorted(self.books)
        return ', '.join(sorted_books)
    
    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'
