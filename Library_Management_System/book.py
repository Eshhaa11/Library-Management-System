class Book:
    def __init__(self, title, author, id):
        self.__title = title
        self.__author = author
        self.__id = id
        self.__is_available = True

    def get_info(self):
        return f"{self.__title} by {self.__author}"

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"📕 Borrowed: {self.__title}")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.__is_available = True
        print(f"📗 Returned: {self.__title}")


class Textbook(Book):
    def __init__(self, title, author, id, subject):
        super().__init__(title, author, id)
        self.__subject = subject

    def get_subject(self):
        return self.__subject
