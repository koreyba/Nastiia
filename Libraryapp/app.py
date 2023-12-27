import pdb
from flask import Flask, render_template, request
import random
from flask import Flask
from classes import Author, Book, Authors_Library, Books_Library, Comment, Library_Printer, Library, DBManager

# Определение экземпляра Flask
app = Flask(__name__)

# Определение маршрутов
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort_authors', methods=['POST'])
def sort_authors():
    sort_method = request.form.get('sort_method')
    library = Library()
    authors = library.authors_lib.get_all_authors()
    if sort_method == 'birth_year':
        authors = library.authors_lib.sort_authors_by_birth_date(authors, True)
        return render_template('authors.html', authors=authors)
    if sort_method == 'alphabet':
        pass # TODO

@app.route('/filter_by_first_later', methods=['POST'])
def filter_aturhos_by_first_later():
    input_value = request.form.get('latter')
    library = Library()
    authors = library.authors_lib.get_all_authors()
    authors = library.authors_lib.get_authors_by_given_letter(authors, input_value)
    return render_template('authors.html', authors=authors)

@app.route('/filter_by_books_count', methods=['POST'])
def filter_authors_by_books_count():
    input_value = int(request.form.get('books_count'))
    library = Library()
    authors = library.authors_lib.get_all_authors()
    authors = library.authors_lib.get_authors_with_n_books(authors, input_value)
    return render_template('authors.html', authors=authors)


@app.route('/sort_books', methods=['POST'])
def sort_books():
    # Логика обработки сортировки авторов
    pass

@app.route('/authors')
def authors():
    library = Library()
    authors = library.authors_lib.get_all_authors()
    return render_template('authors.html', authors=authors)  # предполагается, что у вас есть шаблон authors.html


@app.route('/books')
def books():
    return render_template('books.html')  # предполагается, что у вас есть шаблон authors.html


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)

