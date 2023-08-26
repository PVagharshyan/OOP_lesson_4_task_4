from typing import List
import copy

class Department:
    class Employee:
        _id: int = 0

        def __init__(self, name: str) -> None:
            self._name = name
            self._current_id = self._id
            self.inc_id()

        def __str__(self) -> str:
            return f"name: {self.name}, id: {self.id}"

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, set_name: str) -> None:
            self._name = set_name

        @property
        def id(self) -> int:
            return self._current_id

        @classmethod
        def inc_id(cls) -> None:
            cls._id += 1

    def __init__(self, name: str) -> None:
        self._name = name
        self._employees = []

    def __str__(self) -> str:
        str_list = [f" {item} \n" for item in self._employees]
        str_list = ''.join(str_list)
        return f"list employees:\n{str_list}name: {self.name}"

    def add_employee(self, employee: Employee) -> None:
        self._employees.append(employee)

    @property
    def employees(self) -> List[Employee]:
        return copy.deepcopy(self._employees)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, set_name: str) -> None:
        self._name = set_name

def main() -> None:
    print("!department!")

if __name__ == "__main__":
    main()
