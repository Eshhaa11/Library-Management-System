class Library: 
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f "Book added: {book.get_info()}")

        