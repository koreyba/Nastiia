from __future__ import annotations

import sqlite3
from typing import List, Dict
import random

 
class Author:
    def __init__(self, name, birth_year, id = 0):
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.name = name
        self.birth_year = birth_year
        self.books: list[Book] = [] # Список книг, написанных автором


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


class Library:
    def __init__(self):
        self.db_manager = DBManager("mydatabase.db")

    def get_all_books(self):
        books = self.db_manager.get_all_books()
        return books

    def get_all_authors(self):
        authors = self.db_manager.get_all_authors()
        return authors

    def print_authors(self, list_of_authors: list[Author]):
        for a in list_of_authors:
            print(f'Author: {a.name}, Birth year: {a.birth_year}, Books: {[book.title for book in a.books]}')
            # for b in a.books:
            #     print(b.title)


class DBManager:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.__create_tables()


    def __create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                            id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE NOT NULL,
                            birth_year INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            release_date TEXT NOT NULL,
                            price REAL NOT NULL,
                            author_id INTEGER,
                            FOREIGN KEY (author_id) REFERENCES authors (id))''')
        self.conn.commit()


    def save_author(self, author: Author):
        cursor = self.conn.cursor()

        # Проверка, существует ли уже автор с таким именем
        cursor.execute("SELECT id FROM authors WHERE name = ?", (author.name,))
        data = cursor.fetchone()
        if data is None:
            # Автора нет в базе данных, вставляем новую запись
            cursor.execute("INSERT INTO authors (id, name, birth_year) VALUES (?, ?, ?)",
                        (author.id, author.name, author.birth_year))
            for book in author.books:
                self.save_book(book)
            self.conn.commit()
        else:
            print(f"Автор {author.name} уже существует в базе данных.")


    def save_book(self, book: Book):
        cursor = self.conn.cursor()

        # Проверка, существует ли уже книга с таким названием и автором
        cursor.execute("SELECT id FROM books WHERE title = ? AND author_id = ?", (book.title, book.author.id))
        data = cursor.fetchone()
        if data is None:
            # Книги нет в базе данных, вставляем новую запись
            cursor.execute("INSERT INTO books (id, title, release_date, price, author_id) VALUES (?, ?, ?, ?, ?)",
                        (book.id, book.title, book.release_date, book.price, book.author.id))
            self.conn.commit()
        else:
            print(f"Книга '{book.title}' автора с ID {book.author.id} уже существует в базе данных.")


    def get_all_authors(self) -> List[Author]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, birth_year FROM authors")
        authors_data = cursor.fetchall()

        authors = {id: Author(name, birth_year, id) for id, name, birth_year in authors_data}

        for author in authors.values():
            author.books = self.__get_books_by_author_id(author.id, authors)

        return list(authors.values())


    def __get_books_by_author_id(self, author_id: int, authors: Dict[int, Author]) -> List[Book]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, release_date, price FROM books WHERE author_id = ?", (author_id,))
        books_data = cursor.fetchall()

        return [Book(title, release_date, price, authors[author_id], id) for id, title, release_date, price in books_data]


    def get_all_books(self) -> List[Book]:
        authors = {author.id: author for author in self.get_all_authors()}

        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, release_date, price, author_id FROM books")
        books_data = cursor.fetchall()

        return [Book(title, release_date, price, authors[author_id], id) for id, title, release_date, price, author_id in books_data if author_id in authors]


    def close(self):
        self.conn.close()
