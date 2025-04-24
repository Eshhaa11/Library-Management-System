class Library: 
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.get_info()}")

    def remove_book(self, id):
        for book in self.books:
            if book._Book__id == id:
                self.books.remove(book)
                print(f"🗑️ Book removed with ID: {id}")
                return
        print("❌ Book not found")