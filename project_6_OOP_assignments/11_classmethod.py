class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display(cls):
        return cls.total_books
    
b1 = Book()
b2 = Book()
b3 = Book()
print(Book.display())

   



