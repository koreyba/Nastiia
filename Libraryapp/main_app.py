import copy

from classes import Library

# vowels = "аеиоуыэюя"
# consonants = "бвгджзйклмнпрстфхцчшщъь"

library = Library()
books = library.get_all_books()
books_with_comments = library.load_comments_for_books(books)
for my_book in books_with_comments:
    com = library.get_comments_with_rat_more_then(my_book.comments, 4.00)
    if len(com) != 0:
        book = copy.deepcopy(my_book)
        book.comments = com
        library.print_book_with_comments(book)

"""
получить книги авторов Н-годов, у которых цена больше или меньше значения, напечатать список книг
авторы после 1800 г.р. с книгами цена, которых меньше чем значение.

*написать сортировку книги и авторов по алфавиту, по году рождения и по колличеству книг 
напечатать список книг и их комменты,
напечатать коменты, у которых оценка больше 3

посчитать рейтинг книги, на основе всех оценок
вывести только позитивные коменты/негативные

"""

# print('\n Автор на заданную букву с длинной слов в названии:')
# print()
# books_with_two_words = library.get_books_with_n_words_in_title(all_books, 2)
# authors_of_books_with_two_words = library.get_authors_of_books(books_with_two_words)
# authors_by_L = library.get_authors_by_given_letter(authors_of_books_with_two_words, "Л")
# library.print_authors(authors_by_L)
#
# print('\n Автор на заданную букву с длинной слов в названии 2:')
# print()
# authors_by_L = library.get_authors_by_given_letter(all_authors, "Л")
# books = library.get_books_of_authors(authors_by_L)
# books_with_N_words = library.get_books_with_n_words_in_title(books, 2)
# library.print_books(books_with_N_words)
# library.print_authors(all_authors)
# print('\n Добавление автора: ')
# library.add_new_author()
# print('\n Добавление книги')
# library.add_new_book()