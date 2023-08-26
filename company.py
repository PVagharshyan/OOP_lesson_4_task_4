import department
import copy
from typing import List

class Company:
    def __init__(self, name):
        self._name = name
        self._departments = []

    def __str__(self) -> str:
        departments = self.departments
        str_departments = [f" {item} \n" for item in departments]
        str_departments = ''.join(str_departments)
        return f"departments: \n{str_departments}name: {self.name}"

    def add_department(self, department: department.Department):
        self._departments.append(department)

    @property
    def departments(self) -> List[department.Department]:
        return copy.deepcopy(self._departments)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, set_name: str) -> None:
        self._name = set_name

def main() -> None:
    print("!company!")

if __name__ == "__main__":
    main()
