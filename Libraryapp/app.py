import pdb
from flask import Flask, render_template, request, session
import random
from flask import Flask
from classes import Author, Book, Authors_Library, Books_Library, Comment, Library_Printer, Library, DBManager

# Определение экземпляра Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Определение маршрутов
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sort_authors', methods=['POST'])
def sort_authors():
    sort_method = request.form.get('sort_method')
    library = Library()
    authors = library.authors_lib.get_all_authors()

    filter_letter = session.get('filter_letter')
    session['filter_letter'] = ''
    if filter_letter != '':
        authors = library.authors_lib.get_authors_by_given_letter(authors, filter_letter)

    filter_books_count = session.get('filter_books_count')
    session['filter_books_count'] = None
    if filter_books_count is not None:
        authors = library.authors_lib.get_authors_with_n_books(authors, filter_books_count)

    if sort_method == 'birth_year':
        authors = library.authors_lib.sort_authors_by_birth_date(authors, True)
        return render_template('authors.html', authors=authors)
    
    if sort_method == 'alphabet':
        authors = library.authors_lib.sort_authors_by_name(authors)
        return render_template('authors.html', authors=authors)


@app.route('/filter_by_first_later', methods=['POST'])
def filter_aturhos_by_first_later():
    input_value = request.form.get('latter')
    session['filter_letter'] = input_value
    library = Library()
    authors = library.authors_lib.get_all_authors()
    authors = library.authors_lib.get_authors_by_given_letter(authors, input_value)
    return render_template('authors.html', authors=authors)


@app.route('/filter_by_books_count', methods=['POST'])
def filter_authors_by_books_count():
    input_value = int(request.form.get('books_count'))
    session['filter_books_count'] = input_value
    library = Library()
    authors = library.authors_lib.get_all_authors()
    authors = library.authors_lib.get_authors_with_n_books(authors, input_value)
    return render_template('authors.html', authors=authors)


@app.route('/sort_books', methods=['POST'])
def sort_books():
    sort_method = request.form.get('sort_method')
    sort_order = session.get('sort_order')
    if sort_order is None:
        sort_order = True

    if sort_order:
        sort_order = False
        session['sort_order'] = sort_order
    else:
        sort_order = True
        session['sort_order'] = sort_order

    library = Library()
    books = library.books_lib.get_all_books()

    if sort_method == 'release_date':
        books = library.books_lib.sort_books_by_year(books, sort_order)
        return render_template('books.html', books=books)

    if sort_method == 'alphabet':
        books = library.books_lib.sort_books_by_name(books)
        return render_template('books.html', books=books)


@app.route('/authors')
def authors():
    library = Library()
    authors = library.authors_lib.get_all_authors()
    return render_template('authors.html', authors=authors)  # предполагается, что у вас есть шаблон authors.html


@app.route('/books')
def books():
    library = Library()
    books = library.books_lib.get_all_books()
    return render_template('books.html' , books=books)


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)

