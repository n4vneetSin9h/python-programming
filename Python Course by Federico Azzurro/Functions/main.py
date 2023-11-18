def greet(name: str):
    print(f'Hello, {name}!')


greet('Mario')
greet('Luigi')


def unspecified_parameter_type(name):
    print(f'{name}')


unspecified_parameter_type(100)
unspecified_parameter_type('Nav')


def do_something(name: str, greeting: str = 'Hello'):  # default parameters always comes after the other parameters
    print(f'{greeting}, {name}!')


do_something('Mario')
do_something('Mario', 'Caio')
do_something(greeting='Namaste', name='Nav')


# returning value
def sum_of_numbers(a, b):
    return a + b


def sum_of_numbers_with_type_hinting(a: int, b: int) -> int:
    return a + b


# *args and **kwargs

def greet_people(*persons):
    print(persons)
    for name in persons:
        print(f'Hello {name}!')


greet_people('Mario', 'Luigi', 'Bowser')  # any parameter after *args will require us to mention the keyword


def do_something_with_kwargs(**kwargs):
    print(kwargs)

    print(kwargs['name'])


do_something_with_kwargs(name='Mario', age=10)


# working with * and / when writing functions
def standard_arg(args):
    print(args)


def position_only_args(pos_args, /):
    print(pos_args)


def kwd_only_args(*, kwargs):
    print(kwargs)


def combined_args_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


kwd_only_args(kwargs='b')