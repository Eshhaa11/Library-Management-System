from book import Book, Textbook
from members import Student
from staff import Librarian
from library import Library

def show_menu():
    print("\n====== LIBRARY MENU ======")
    print("1. View all books")
    print("2. Add a book (Staff)")
    print("3. Remove a book (Staff)")
    print("4. Borrow a book (Student)")
    print("5. Return a book (Student)")
    print("6. Exit")
    print("==========================")


library = Library()
librarian = Librarian("Mr. John", "L001")
student = Student("Alice", "S001")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        id = input("Enter ID: ")
        book = book(title, author, id)
        librarian.add_book(library, book)

    elif choice == "3":
        id = input("Enter IDof book to remove: ")
        library.remove_book(id)

    elif choice == "4":
        id = input("Enter ID of book to borrow: ")
        for book in library.books:
            if book._Book__id == id:
                student.borrow_book(book)
                break
        else:
            print("Book not found.")

    elif choice == "5":
        id = input("Enter ID of book to return: ")
        for book in library.books:
            if book._Book__id == id:
                student.return_book(book)
                break
        else:
            print("Book not found.")

    elif choice == "6":
        print("👋 Exiting Library. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
