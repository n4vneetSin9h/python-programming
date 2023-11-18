import math

print(abs(-67))

max([56, 67, 8, 51])

names: list[str] = ['Robert', 'Mario', 'Peach', 'Tom']

for idx, name in enumerate(names):
    print(f'{idx} : {name}')

number = 15.65666

print(round(number, 2))

numbers = range(0, 10, 2)

print(list(numbers))

also_negative_numbers = range(30, -25, -5)

print(list(also_negative_numbers))

global_variable = 'GLOBAL'


def global_function():
    local_int_variable: int = 45
    local_str_variable: str = 'abc'

    def local_function():
        pass

    print(locals())

    return 'GLOBAL'


class Car:
    def __init__(self):
        print('GLOBAL')


print('List of globals:', globals())

global_function()

is_connected: bool = True
has_electricity: bool = True
has_paid_bill: bool = True
requirements: list[bool] = [is_connected, has_electricity, has_paid_bill]
internet_working: bool = all(requirements)  # requires all elements to be true

print(internet_working)

knows_how_to_drive: bool = True
is_own_vehicle: bool = False
is_registered_in_own_name: bool = False
driving_requirements: list[bool] = [knows_how_to_drive, is_own_vehicle, is_registered_in_own_name]
can_drive: bool = any(driving_requirements)

print(can_drive)

random_list: list[str, int] = ['Mario', 45, 46, 'Luigi', 34, 6, 'Darius', 'Ria', 'Naomi', 4, 23, 69, 'Ron', 34, 'Harry',
                               46, 'Hermoine', 94, 75, 80]


def is_str(element):
    return isinstance(element, str)


filtered_people: list[str] = list(filter(is_str, random_list))

print(filtered_people)

random_numbers: list[int] = [45, 65, 1, 34, 57, 98, 36, 48, 69]


def double_the_element(element):
    return element * 2


doubled_numbers: list[int] = list(map(double_the_element, random_list))

print(doubled_numbers)

unsorted_list: list[int] = [45, 65, 1, 34, 57, 98, 36, 48, 69]

sorted_random_numbers = random_numbers.sort()

sorted_list = sorted(unsorted_list, reverse=True)

print(sorted_random_numbers)
print(random_numbers)
print(sorted_list)


class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f'{self.name}: {self.calories} kcal'


fruit_basket: list[Fruit] = [Fruit('Apple', 100),
                             Fruit('Mango', 250),
                             Fruit('Ananas', 150),
                             Fruit('Strawberry', 200)]


def sort_by_calories(fruit: Fruit):
    return fruit.calories


sorted_fruit_basket: list[Fruit] = sorted(fruit_basket, key=sort_by_calories)

print(sorted_fruit_basket)

# user_input: str = input('Input your math: ')
# result: float = eval(user_input)
# print(result)

# source_code: str = input('Input your code: ')
# exec(source_code)


list_one: list[str] = ('Mario', 'Luigi', 'Toad', 'Bowser')
list_two = (10, 20, 30, 40)
zipped = zip(list_one, list_two)

for name, number in zipped:
    print(name, number, sep=':')