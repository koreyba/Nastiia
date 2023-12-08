from __future__ import annotations

import random

 
class Author:
    def __init__(self, name, birth_year, id = 0):
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.name = name
        self.birth_year = birth_year
        self.books = []  # Список книг, написанных автором


    def add_book(self, book: Book):
        self.books.append(book)


class Book:
    def __init__(self, title: str, release_date, price, author: Author, id = 0):
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.title = title
        self.release_date = release_date
        self.price = price
        self.author: Author = author  # Экземпляр класса Author



