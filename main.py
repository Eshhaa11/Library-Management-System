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

    def return_book(self):
        self.__is_available = True
        print(f"  Returned: {self.__title}")

    class Textbook(Book):
        def __init__(self, title, author, isbn, subject):
            super().__init__(title, author, isbn)
            self.__subject = subject

    
        def get_subject(self):
            return self.__subject
        
    class Member:
        def __init__(self, name, member_id):
            self._name = name
            self._member_id = member_id
            self._borrowed_books = []

        def  get_name(self):
            return self._name
        
    class Student(Member):
        def __init__(self, name, member_id):
            

            

