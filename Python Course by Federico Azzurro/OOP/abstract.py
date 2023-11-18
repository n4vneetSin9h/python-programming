from abc import ABC, abstractmethod
from typing import Protocol


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        ...

    @abstractmethod
    def call_target(self, person: str):
        ...


class IBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    def call_target(self, person: str):
        print(f'calling {person}')

    @property
    def power(self):
        raise NotImplementedError('Code missing...')


class Printable(Protocol):
    pages: int

    def print(self):
        pass

    def recycle(self):
        pass


class Book:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print(f'Printing book: {self.title}')

    def recycle(self):
        print(f'Recycling book: {self.title}')


class Magazine:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print(f'Printing magazine: {self.title}')

    def recycle(self):
        print(f'Recycling magazine: {self.title}')


def print_item(printable: Printable):
    printable.print()


def recycle_item(printable: Printable):
    printable.recycle()


class Connection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('Connecting...')
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print('WARNING: Connection already exists')
            return cls.__instance

    def __init__(self):
        print('Connected to the internet')


if __name__ == '__main__':
    phone = IBanana('Android')
    phone.call_target('ash')

    book: Printable = Book('Python')
    print_item(book)
    recycle_item(book)

    magazine: Printable = Magazine('Vogue')
    print_item(magazine)
    recycle_item(magazine)

