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

    def update_book(self, id, new_title=None, new_author=None):
        for book in self.books:
            if book._Book__id == id:
                if new_title:
                    book._Book__title = new_title
                if new_author == new_author:
                    book._Book__author = new_author

                print("Book Information Updated Successfuly")