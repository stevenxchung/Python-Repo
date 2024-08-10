from typing import List, Protocol


class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def get_lastname(self) -> str:
        return self.lastName

    def get_age(self) -> int:
        return self.age

    def is_married(self) -> bool:
        return self.married


class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool: ...


class AdultFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.age >= 18


class SeniorFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.age >= 65


class MarriedFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.is_married()


class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def set_filter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        filtered = [p for p in people if self.filter.apply(p)]
        res = len(filtered)
        print(f'count(): {res}')
        return res


if __name__ == '__main__':
    people = [
        Person('Doe', 20, False),
        Person('Smith', 30, True),
        Person('Old', 70, True),
    ]

    counter = PeopleCounter()

    counter.set_filter(AdultFilter())
    counter.count(people)  # Adult count: 3

    counter.set_filter(SeniorFilter())
    counter.count(people)  # Senior count: 1

    counter.set_filter(MarriedFilter())
    counter.count(people)  # Married count: 2
