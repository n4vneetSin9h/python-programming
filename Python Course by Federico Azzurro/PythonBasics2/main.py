import sample
from enum import Enum

# file = open('sample.txt')
# text = file.read()
# file.close()

with open('sample.txt') as file:
    text = file.read()
    print(text)


def greet():  # use Shift + fn + f6 to refactor
    print("hello, mom")


greet()
greet()

var = ''

if bool(var):
    print('contains characters')
else:
    print('empty variable')

# False value by bool
empty_list = []
empty_tuple = ()
empty_set = set()
empty_string = ''
empty_range = range(0)

zero_int = 0
zero_float = 0.0
zero_complex = complex(0j)
none = None


# Enums
class State(Enum):
    OFF = 0
    ON = 1


state = State.ON

if state == State.ON:
    print('Lamp is turned on!')
elif state == State.OFF:
    print('Lamp is turned off!')


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


color = Color.RED

if color == Color.RED:
    print(color)
elif color == Color.BLUE:
    print(color)
elif color == Color.GREEN:
    print(color)

# Comparing Floats

floatA = 0.3
floatB = 0.1 + 0.2

print(floatA)  # 0.3
print(floatB)  # 0.300000000...
print(floatA == floatB)  # False


def compare_floats(a: float, b: float, tol: float) -> bool:
    absolute = abs(a - b)
    print(f'{a} - {b} = {a - b}')
    return absolute < tol


first = 0.8
second = 0.7 + 0.1

print(compare_floats(first, second, 1e-10))

print(__name__)
sample.do_something()

globalVariable = 10


def func():
    global globalVariable
    global newVariable
    x = 20
    print('Inner', x)

    def inner_func():
        nonlocal x
        x = 10
        print('Inner func', x)

    inner_func()


func()

print('Outer', globalVariable)

sample_list = []

for i in range(10):
    if i % 2 == 0:
        sample_list.append(i)

print(sample_list)

sample_list2 = [i for i in range(10) if i % 2 == 0]
sample_list3 = [i * 2 for i in range(10) if i % 2 == 0]

print(sample_list2)


people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']

cap_people = [person for person in people]

print(cap_people)


# slices
numbers: list[int] = list(range(22))

print(numbers[:3])
print(numbers[::3])
print(numbers[2:6])
print(numbers[1::3])
print(numbers[10:16:2])
print(numbers[10:])


