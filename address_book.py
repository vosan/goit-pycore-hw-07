from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __str__(self):
        return self.value.title()


class Phone(Field):
    def __init__(self, value):
        v = str(value).strip()
        if not (len(v) == 10 and v.isdigit()):
            raise ValueError("Incorrect phone number format.")
        super().__init__(v)


class Birthday(Field):
    def __init__(self, value):
        try:
            if isinstance(value, datetime):
                dt = value
            else:
                s = str(value).strip()
                if not s:
                    raise ValueError("Invalid date format. Use DD.MM.YYYY")
                dt = datetime.strptime(s, "%d.%m.%Y")
            super().__init__(dt)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")




class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                del self.phones[i]
                return True
        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
