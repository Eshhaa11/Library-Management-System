# 📚 Library Management System — Python OOP Project

This is a **text-based Library Management System** created as part of a Python Object-Oriented Programming (OOP) assignment.

It uses OOP concepts like **classes**, **inheritance**, **encapsulation**, and **modularity** to simulate a real-world library, where students and faculty can borrow books, and staff can manage them.

---

## 🧠 Project Purpose

To demonstrate understanding of:
- Class design and inheritance
- Encapsulation and data protection
- Functional interaction through a simple UI
- Code modularity and organization

---

## 💡 Features

✅ Encapsulated book data with `title`, `author`, and unique `ID`  
✅ Student and Faculty members with different borrowing limits  
✅ Staff roles like Librarian with permissions to manage books  
✅ Borrow and return system with availability tracking  
✅ User-friendly command-line menu system  
✅ Modular code: each class in a separate file

---

## 📁 Folder Structure

```
LibraryManagementSystem/
│
├── book.py        # Book & Textbook classes
├── member.py      # Member, Student, Faculty classes
├── staff.py       # Staff and Librarian classes
├── library.py     # Library class - manages the collection
├── main.py        # Runs the system, includes user menu
└── README.md      # Project documentation
```

---

## ⚙️ Installation & Running the Project

> 🧪 Prerequisites: Python 3.x

1. 📅 Download or clone this repository:
   ```bash
   git clone https://github.com/Eshhaa11/OOP-Project
   cd OOP-project
   ```

2. ▶️ Run the program:
   ```bash
   python main.py
   ```

3. 💻 Follow the menu prompts to interact with the system

---

## 🧑‍🎓 Roles in the System

### 📕 Books
- Each book has a `title`, `author`, and `id`
- Encapsulated using `self.__title`, etc.
- Methods to check availability, borrow, return, display info

### 👥 Members
- Base class: `Member`
- Two types: `Student` and `Faculty`
- Can borrow and return books
- Borrow limits: Students (3), Faculty (5)

### 🧑‍🎼 Staff
- Base class: `Staff`
- `Librarian` inherits and can:
  - Add new books
  - Remove books from library
  - View collection

### 🏩 Library
- Maintains list of all books
- Handles searching, listing, and removing books

---

## 📋 Menu Options (User Interface)

When you run the program, you'll see this menu:

```
====== LIBRARY MENU ======
1. View all books
2. Add a book (Staff)
3. Remove a book (Staff)
4. Borrow a book (Student)
5. Return a book (Student)
6. Exit
==========================
```

---

## 🧪 Example Usage

> Adding a new book:
```
Enter book title: Atomic Habits
Enter author: James Clear
Enter book ID: A101
```

> Borrowing a book:
```
Enter book ID to borrow: A101
📕 Borrowed: Atomic Habits
```

> Returning a book:
```
Enter book ID to return: A101
Returned: Atomic Habits
```

---

## 🧰 Object-Oriented Concepts Used

| Concept        | How It's Used                                     |
|----------------|---------------------------------------------------|
| Class          | `Book`, `Library`, `Student`, etc.                |
| Object         | `book1 = Book(...)`                               |
| Inheritance    | `Textbook(Book)`, `Student(Member)`               |
| Encapsulation  | Private variables like `self.__id`                |
| Composition    | `Library` contains a list of `Book` objects       |
| Aggregation    | `Librarian` can add/remove `Book` from `Library` |

---

## ✨ What You'll Learn

- How to split a program into classes and modules
- Real-world modeling of roles and actions
- Private vs public data in Python
- Text-based interaction using `input()` and loops
- Clean and maintainable code structure



---

## 🧾 Author & License

Developed by: *Esha Patel*  
License: Free to use for educational purposes 👨‍🏫

---

## 🙌 Thanks for Reading

If this helped you learn OOP, feel free to ⭐️ this repo and share it!

Happy Coding! 🧑‍💻

