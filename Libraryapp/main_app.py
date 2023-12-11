from classes import Library

library = Library()
all_authors = library.get_all_authors()
library.print_authors(all_authors)
all_books = library.get_all_books()
library.print_books(all_books)
print('======')
library.print_books_after_1900y(all_books)
print('=======')
library.print_authors_by_letter(all_authors, 'М')
print('=======')
library.print_authors_with_more_than_N_books(all_authors, 2)
print('========')
authors_with_N_book = library.print_authors_whith_N_books(all_authors, 0)

"""вывести все книги, включая год и все такое
вывести книги после 1900года
вывсти авторов на заданную букву
вывести автров, у которых больше одной книги
вывести авторов, у которых больше двух книг (с списком книг)
вывести авторов, у которых нет книг
вывести книги, у которых в названии три слова
Для авторов, у которых N книг - менять им имена (авторам - например добавить знак!)"""