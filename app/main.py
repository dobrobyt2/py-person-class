class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = []
    for data in people:
        new_person = Person(data["name"], data["age"])
        person_list.append(new_person)

    for data in people:
        current_person = Person.people[data["name"]]

        if "husband" in data and data["husband"] is not None:
            current_person.husband = Person.people[data["husband"]]

        if "wife" in data and data["wife"] is not None:
            current_person.wife = Person.people[data["wife"]]

    return person_list
