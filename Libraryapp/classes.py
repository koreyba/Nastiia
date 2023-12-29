from __future__ import annotations

import sqlite3
from typing import List, Dict
import random



class Comment:
    def __init__(self, text: str, rating: float, is_positive: bool, id = 0):
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.text = text
        self.rating = rating
        self.is_positive = is_positive

    def is_comment_rat_is_more_then(self, n):
        if self.rating > n:
            return True
        else:
            return False

class Author:
    def __init__(self, name, birth_year, id = 0):
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.name: str = name
        self.birth_year: int = birth_year
        self.books: list[Book] = [] # Список книг, написанных автором

    def add_book(self, book: Book):
        self.books.append(book)

    def is_author_has_n_books(self, n):
        if len(self.books) == n:
            return True
        else:
            return False

    def is_author_has_books_more_then(self, n):
        if len(self.books) > n:
            return True
        else:
            return False


class Book:
    bla = 0

    def __init__(self, title: str, release_date, price, author: Author, id = 0):
        Book.bla += 1
        if id == 0:
            self.id = random.randint(3000, 10000000)
        else:
            self.id = id
        self.title: str = title
        self.release_date: int = release_date
        self.price: float = price
        self.author: Author = author  # Экземпляр класса Author
        self.comments: list[Comment] = []  # List to store comments

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments_with_rat_more_then(self, n):
        list_of_comments = []
        for comment in self.comments:
            if comment.is_comment_rat_is_more_then(n):
                list_of_comments.append(comment)
        return list_of_comments

    def get_rating(self):
        sum = 0
        for comment in self.comments:
            sum += comment.rating
        return round(sum / len(self.comments), 2)

    def get_comments(self, only_positive: bool):
        return [comment for comment in self.comments if comment.is_positive == only_positive]


class Library_Printer:
    def print_authors(self , list_of_authors: list[Author]):
        for a in list_of_authors:
            print(f'Author: {a.name}, Birth year: {a.birth_year}, Books: {[book.title for book in a.books]}')
            # for b in a.books:
            #     print(b.title)

    def print_books(self , list_of_books: list[Book] , to_print_authors=True):
        for book in list_of_books:
            if to_print_authors is True:
                print(f'Book: {book.title}, Release date: {book.release_date}, Price: {book.price}, Author: {book.author.name}')
            else:
                print(f'Book: {book.title}, Release date: {book.release_date}')

    def print_comments(self, list_of_com: list[Comment]):
        for comment in list_of_com:
            print(f'Text: {comment.text}, Ratio: {comment.rating}, +/-: {comment.is_positive}')

    def print_book_with_comments(self, book: Book):
        comments_str = [f"Text: {comment.text}, Ratio: {comment.rating}, +/-: {str(comment.is_positive)}" for comment in book.comments]

        print(f'Book: {book.title}, Comments: {comments_str}')


class Authors_Library:
    def __init__(self):
        self.db_manager = DBManager("mydatabase.db")

    def get_all_authors(self):
        authors = self.db_manager.get_all_authors()
        return authors

    def get_authors_by_given_letter(self, list_of_authors: list[Author], let: str):
        list_a = []
        for author in list_of_authors:
            if author.name[0] == let:
                list_a.append(author)
        return list_a

    def get_authors_with_more_than_n_books(self, list_of_authors: list[Author], N):
        list_a = []
        for author in list_of_authors:
            if author.is_author_has_books_more_then(N):
                list_a.append(author)
        return list_a

    def get_authors_with_n_books(self, list_of_authors: list[Author], N):
        list_a = []
        for a in list_of_authors:
            if a.is_author_has_n_books(N):
                list_a.append(a)
        return list_a

    def get_books_of_authors(self, list_of_authors: list[Author]):
        list_of_books: list[Book] = []
        for author in list_of_authors:
            for book in author.books:
                list_of_books.append(book)

        return list_of_books

    def get_authors_birth_year_after(self, list_of_authors: list[Author], year: int):
        list_of_birth = []
        for author in list_of_authors:
            if author.birth_year > year:
                list_of_birth.append(author)
        return list_of_birth

    def get_authors_birth_year_before(self, list_of_authors: list[Author], year: int):
        list_of_birth = []
        for author in list_of_authors:
            if author.birth_year < year:
                list_of_birth.append(author)
        return list_of_birth

    def add_new_author(self):
        name = input("Enter author name: ")
        birth_year = input("Enter author's year of birth: ")
        author = Author(name, birth_year)
        self.db_manager.save_author(author)

    def get_author_by_name(self, authors: list[Author], name):
        for author in authors:
            if author.name == name:
                return author

    def get_authors_by_vowels_letter(self, list_of_author: list[Author], first_letter):
        authors_list = []
        for author in list_of_author:
            if author.name[0].lower() in first_letter:
                authors_list.append(author)
        return authors_list

    def sort_authors_by_birth_date(self, list_of_author: list[Author], is_ascending: bool):
        for i in range(len(list_of_author)):
            author = list_of_author[i]
            j = i - 1
            if is_ascending:
                while list_of_author[j].birth_year < author.birth_year and j >= 0:
                    j = self.__swap_authors_in_list__(author, j, list_of_author)
            else:
                while list_of_author[j].birth_year > author.birth_year and j >= 0:
                    j = self.__swap_authors_in_list__(author, j, list_of_author)
        return list_of_author

    def __swap_authors_in_list__(self, author, j, list_of_author):
        temp = list_of_author[j]
        list_of_author[j] = author
        list_of_author[j + 1] = temp
        j = j - 1
        return j

    def sort_authors_by_name(self, list_of_authors: list[Author]):
        return sorted(list_of_authors, key=lambda x: x.name)

class Books_Library:
    def __init__(self):
        self.db_manager = DBManager("mydatabase.db")

    def get_all_books(self):
        books = self.db_manager.get_all_books()
        return books

    def load_comments_for_books(self, list_of_books: list[Book]):
        for book in list_of_books:
            book.comments = self.db_manager.get_comments_by_book_id(book.id)
        return list_of_books

    def get_books_since_given_year(self, list_of_books: list[Book], date):
        list_b = []
        for book in list_of_books:
            if int(book.release_date) > date:
                list_b.append(book)
        return list_b

    def get_books_with_n_words_in_title(self , list_of_books: list[Book], N):
        list_b = []
        for book in list_of_books:
            words = book.title.split()
            len_of_list = len(words)
            if len_of_list == N:
                list_b.append(book)
        return list_b

    def get_authors_of_books(self, list_of_books: list[Book]):
        list_of_authors: list[Author] = []
        for book in list_of_books:
            list_of_authors.append(book.author)

        return list_of_authors

    def gef_price_of_book_lower_then(self, list_of_books: list[Book], price: float):
        price_list = []
        for book in list_of_books:
            if book.price < price:
                price_list.append(book)
        return price_list

    def gef_price_of_book_higher_then(self, list_of_books: list[Book], price: float):
        price_list = []
        for book in list_of_books:
            if book.price > price:
                price_list.append(book)
        return price_list

    def add_new_book(self):
        title = input("Enter book title: ")
        release_date = input("Enter book's release date: ")
        price = input("Enter book's price: ")
        name = input("Enter author name: ")
        authors = self.db_manager.get_all_authors()
        author = Authors_Library().get_author_by_name(authors, name)
        book = Book(title, release_date, price, author)
        self.db_manager.save_book(book)

    def get_books_with_n_letter_in_i_word(self, list_of_books: list[Book], n: str, index):
        book_list = []
        for book in list_of_books:
            words = book.title.split()
            if len(words) > index and words[index].startswith(n):
                book_list.append(book)
        return book_list

    def sort_books_by_year(self, list_of_books: list[Book], is_ascending: bool):
        for i in range(len(list_of_books)):
            book = list_of_books[i]
            j = i - 1
            if is_ascending:
                while list_of_books[j].release_date < book.release_date and j >= 0:
                    j = self.__swap_books_in_list__(book, j, list_of_books)
            else:
                while list_of_books[j].release_date > book.release_date and j >= 0:
                    j = self.__swap_books_in_list__(book, j, list_of_books)
        return list_of_books

    def __swap_books_in_list__(self, book, j, list_of_books):
        temp = list_of_books[j]
        list_of_books[j] = book
        list_of_books[j + 1] = temp
        j = j - 1
        return j

    def sort_books_by_name(self, list_of_books: list[Book]):
        return sorted(list_of_books, key=lambda x: x.title)


class Library:
    def __init__(self):
        self.db_manager = DBManager("mydatabase.db")
        self.printer = Library_Printer()
        self.authors_lib = Authors_Library()
        self.books_lib = Books_Library()


class DBManager:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.__create_tables()
        
    
    def save_comment(self, comment: Comment, book: Book):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO comments (id, text, rating, is_positive, book_id) VALUES (?, ?, ?, ?, ?)",
                       (comment.id, comment.text, comment.rating, comment.is_positive, book.id))
        self.conn.commit()


    def get_comments_by_book_id(self, book_id: int) -> List[Comment]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, text, rating, is_positive FROM comments WHERE book_id = ?", (book_id,))
        comments_data = cursor.fetchall()
        return [Comment(text, rating, bool(is_positive), id) for id, text, rating, is_positive in comments_data]


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
        cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                            id INTEGER PRIMARY KEY,
                            text TEXT NOT NULL,
                            rating REAL NOT NULL,
                            is_positive BOOLEAN NOT NULL,
                            book_id INTEGER,
                            FOREIGN KEY (book_id) REFERENCES books (id))''')
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
            author.books = self.__get_books_by_author_id(author.id , authors)

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
