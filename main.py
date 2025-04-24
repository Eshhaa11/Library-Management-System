class Book: 
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
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
