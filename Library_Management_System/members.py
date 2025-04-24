class Member:
        def __init__(self, name, member_id):
            self._name = name
            self._member_id = member_id
            self._borrowed_books = []

        def  get_name(self):
            return self._name
        
class Student(Member):
        def __init__(self, name, member_id):
            super().__init__(name, member_id)
            self._borrow_limit = 3

class Faculty(Member):
        def __init__(self, name, member_id):
            super().__init__(name, member_id)
            self._borrow_limit = 5
