from classes import Library

library = Library()
all_authors = library.get_all_authors()
all_books = library.get_all_books()
books_by_year = library.get_books_since_given_year(all_books, 1900)
authors_by_letter = library.get_authors_by_given_letter(all_authors , 'Л')
n_book_authors = library.get_authors_with_more_than_n_books(all_authors , 2)
authors_with_N_book = library.get_authors_with_n_books(all_authors , 1)
n_words_books = library.get_books_with_n_words_in_title(all_books , 4)

library.print_authors(authors_by_letter)
print('\n')
library.print_authors(n_book_authors)
print('\n')
library.print_authors(authors_with_N_book)
print('\n')
library.print_books(all_books)
print('\n')
library.print_books(books_by_year)
print('\n')
library.print_books(n_words_books)



"""вывести авторов на букву Л, у которых в названии книги больше чем одно слово
добавить новую книгу в базу данных
добавить нового автора в БД
вывести авторов, имя которых на Л либо на М
вывести авторов, у которых год рождения меньше чем 2000 и больше чем 1900"""