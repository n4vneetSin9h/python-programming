class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(self.model, ' is turned on.')

    def turn_off(self):
        print(self.model, ' is turned off.')

    def describe(self):
        print(f'Lamp: {self.model} ({self.color})')


lamp = Lamp('MOGX77', 'Red')
lamp.turn_on()
lamp.turn_off()
lamp.color = 'Green'
lamp.describe()


class Animal:
    tricks: list[str] = []

    def __init__(self, name: str):
        self.name = name

    def teach_trick(self, trick_name: str):
        self.tricks.append(trick_name)


class Fruit:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):  # acts as getter
        print(f'{self.__name} is being accessed!')
        return self.__name

    @name.setter
    def name(self, value: str):
        print(f'{self.__name} is now {value}')
        self.__name = value


class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.model} ({self.color})'

    def __repr__(self):
        return f'Car(model={self.model}, color={self.color})'


class Laptop:
    def __init__(self, brand: str, model: int, color: str):
        self.brand = brand  # public
        self._color = color  # protected
        self.__model = model  # private


class Notebook(Laptop):
    def __init__(self, brand: str, model: int, color: str):
        super().__init__(brand, model, color)

    def do_something(self):
        print(self._color)


class Calculator:

    model: int = 45

    def __init__(self, name: str):
        self.name = name

    def description(self):
        print(f'{self.name} is a calculator!')

    @staticmethod
    def add_numbers(a: float, b: float):
        print(a+b)

    @classmethod
    def created_with_version(cls, name: str, model: int):
        cls.model = model
        return cls(f'{name}: ({model})')

if __name__ == '__main__':
    dog: Animal = Animal('Bones')
    cat: Animal = Animal('Tom')

    dog.teach_trick('Make dinner!')
    dog.teach_trick('Go work at job')

    print('Dog tricks:', dog.tricks)
    print('Cat tricks:', cat.tricks)

    apple = Fruit('red apple')
    print(apple.name)

    car: Car = Car('BMW', 'Blue')
    print(car)
    print(car.__repr__())

    laptop = Laptop('Apple', 2021, 'space grey')
    print(laptop._Laptop__model)

    notebook = Notebook('Apple', 2021, 'rose gold')
    notebook.do_something()

    calc = Calculator('casio')
    calc.description()

    Calculator.add_numbers(3, 5)
    newCalc = Calculator.created_with_version('philips', 1992)
    newCalc.description()
    