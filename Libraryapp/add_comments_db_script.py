from faker import Faker
from classes import Comment, Library, DBManager


library = Library()
db_manager = DBManager('mydatabase.db')

books = library.get_all_books()
for book in books:
    fake = Faker()
    comment = Comment(fake.sentence(), round(fake.random.uniform(0, 5), 2), fake.boolean())
    book.add_comment(comment)
    db_manager.save_comment(comment, book)