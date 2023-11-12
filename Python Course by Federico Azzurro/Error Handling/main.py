def do_something(request_str: str = 'Enter a number: '):
    user_input = input(request_str)

    try:
        number = float(user_input)
        if number <= 0:
            raise Exception('Only positive numbers allowed')
        print(number)
    except ValueError:
        do_something('Please enter a valid number: ')
    except Exception as e:
        print('Something went wrong... ', e)
    else:
        print('Will run if successfully executed the code!')
    finally:
        print('Will always be executed!')


do_something()