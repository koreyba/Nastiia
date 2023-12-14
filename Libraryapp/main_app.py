from classes import Library

library = Library()
all_authors = library.get_all_authors()
all_books = library.get_all_books()
print('Все книги')
print()
library.print_books(all_books)

books_by_year = library.get_books_since_given_year(all_books, 1900)
print('Книги за заданным годом')
print()
library.print_books(books_by_year)

authors_by_letter = library.get_authors_by_given_letter(all_authors, 'Л')
print('Авторы за заданной буквой:')
print()
library.print_authors(authors_by_letter)

n_book_authors = library.get_authors_with_more_than_n_books(all_authors, 2)
print('Авторы с больше чем Н-ым колличеством книг')
print()
library.print_authors(n_book_authors)

authors_with_N_book = library.get_authors_with_n_books(all_authors, 1)
print('Авторы с Н-ым колличеством книг')
print()
library.print_authors(authors_with_N_book)

n_words_books = library.get_books_with_n_words_in_title(all_books, 2)
print('Книги с Н-ым колличество слов')
print()
library.print_books(n_words_books)

authors_birth = library.get_authors_between_two_years_of_born(all_authors, 2000, 1900)
print('\n Дата рождения авторов:')
print()
library.print_authors(authors_birth)


"""добавить новую книгу в базу данных
добавить нового автора в БД
вывести авторов, имя которых на Л либо на М
чтобы метод принта книг принимал параметр булевый to_print_authors, который бы был по умолчанию тру. 
Но если передают фолс, то чтобы авторы не печатались
вывести книги авторов на букву Л либо М, которые родились между годами Х/У
вывести книги, если их автор имеет больще двух книг
вывести книги, у которых второе слово в названии начинается с буквы ""
"""

print('\n Автор на заданную букву с длинной слов в названии:')
print()
books_with_two_words = library.get_books_with_n_words_in_title(all_books, 2)
authors_of_books_with_two_words = library.get_authors_of_books(books_with_two_words)
authors_by_L = library.get_authors_by_given_letter(authors_of_books_with_two_words, "Л")
library.print_authors(authors_by_L)

print('\n Автор на заданную букву с длинной слов в названии 2:')
print()
authors_by_L = library.get_authors_by_given_letter(all_authors, 'Л')
books = library.get_books_of_authors(authors_by_L)
books_with_N_words = library.get_books_with_n_words_in_title(books, 2)
library.print_books(books_with_N_words)