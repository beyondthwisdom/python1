# book_manager/book_manager.py

from book_manager.book import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
