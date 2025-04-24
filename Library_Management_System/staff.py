class Staff:
    def __init__(self, name, staff_id):
        self._name = name
        self._staff_id = staff_id


class Librarian(Staff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)

    def add_book(self, library, book):
        library.add_book(book)

    def issue_fine(self, member, amount):
        print(f"💵 {member.get_name()} fined ${amount}")
