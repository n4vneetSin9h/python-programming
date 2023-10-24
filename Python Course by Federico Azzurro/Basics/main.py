greeting: str = "Hello"

print(greeting + ", Mom!")
print(greeting + ", Dad!")
print(greeting + ", Bro!")

happy_thoughts = "Happy"  # Python uses snake case

PI = 3.1415  # Python doesn't have the concept of constants as it's a dynamically typed language, but we do use
# capital naming convention to make it explicit that this is supposed to be a constant

text = "text"  # string
number = 100
decimal = 12.5
complex_number = 3j

people = ["Mario", "Luigi"]

lotto_number = (1, 2, 3, 4, 5, 6)  # tuple concept but it's different compared to Swift

numbers = range(1, 1000)  # 1...999

users = {'user1': 'mario_123', 'user2': 'Luigi'}  # dictionaries

unique_numbers = {1, 2, 2, 3, 3, 4}  # sets will print {1, 2, 3, 4}, and there is no specific order

unique_numbers2 = frozenset(unique_numbers)  # creates a non editable set

is_connected = True

is_empty = None

type_converted_string: str = str(number)

a = 5
b = 6

a **= 3  # 5^3

print(a)  # 125

print(a > b and 5 >= 6)

print(a > 5 or 0 < b)

print(not False)  # True

a = 100.0
b = 1.0 * a

print(id(a))
print(id(b))
print(a is b)  # False - looks for id (memory address) can be same in certain cases
print(a is not b)
print(1 in unique_numbers2)

peoples: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']
peoples2: list[str] = ['Sonic', 'Tails']

print(peoples[-4])
print(peoples[-3])
print(peoples[-2])
print(peoples[-1])
print(peoples[0])
print(peoples[1])
print(peoples[2])
print(peoples[3])
print(peoples[0:4])  # last index is not included (0..<4)

print('Luigi' in peoples)

peoples[0:2] = ['Shy Guy', 'Bowser']

peoples.append('Mario')

new_peoples_list = peoples + peoples2
# alternate ways: peoples += peoples2
# alternate ways: peoples.extend(peoples2)

new_peoples_list.remove('Mario')

print(new_peoples_list)
new_peoples_list.pop()  # removes last element

print(new_peoples_list)
new_peoples_list.pop(2)  # removes 2nd index

print(new_peoples_list)

peoples.sort()  # sorts alphabetically
peoples.reverse()  # reverses the list
new_peoples_list.clear()  # removes everything

people_tuple: tuple = 'Mario', 'Luigi', 'Peach',  # last comma is important and you can surround this with parenthesis
people_list: list[str] = list(people_tuple)
print(people_list.count('Mario'))  # looks for occurrences of 'Mario'

a, b, c, = people_tuple  # unpacks tuples

e, *f = people_list  # e will be first element and f will be rest of the elements

items: set = {'apple', 10, True, 'banana'}

items.add('watermelon')

# items.remove('apple')  # removes the element if it exists in the set and throws error if it doesn't exist
# items.discard('apple')  # removes the element if it exists in the set and doesn't throw any error if it doesn't exist

items2: set = {'orange', 'grapes', 'apple', 10}

# items |= items2  # same as Union method with re-assignment
new_intersection = items.intersection(items2)
new_set = items.symmetric_difference(items2)

empty_set = set()

print(new_intersection)
print(new_set)

empty_dictionary = {}

usernames: dict = {'user1': 'Mario',
                   'user2': 'Luigi'}

user_list = list(usernames.items())  # items() returns a list of tuples
user_dict_values_list = list(usernames.values())

random_key = 'XX'
print(users.setdefault(random_key, f'There is no {random_key} key'))
