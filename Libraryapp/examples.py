from classes import DBManager
from classes import Book, Author

# Connect to DB:
db_manager = DBManager("mydatabase.db")

# How to add a new Author w ith his books:
author = Author('Nastia', 1992)
book = Book("Never written book", 2023, 0, author)
author.add_book(book)
# Save author with already added books to DB:
db_manager.save_author(author)

# How to add a new book to existing author:
authors = db_manager.get_all_authors()
existing_author = authors[0]
book = Book("My book", 2023, 0, existing_author)

#save book to DB:
db_manager.save_book(book)

#Print all books and authors:
books = db_manager.get_all_books()

for author in authors:
    print(f"Автор: {author.name}, Книги: {[book.title for book in author.books]}")

for book in books:
    print(f"Книга: {book.title}, Дата релиза {book.release_date}, Автор: {book.author.name} ")

# Close DB connection:
db_manager.close()

