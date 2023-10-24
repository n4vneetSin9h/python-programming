# if...else
a = 10
b = 5

if a > b:
    print(f'{a} is more than {b}')
else:
    print(f'{b} is more than {a}')

print(f'{a} is more than {b}') if a > b else print(f'{b} is more than {a}')  # shorthand way of executing if...else

if a > b:
    print("Hello!")
elif a == b:
    print("Goodbye!")
else:
    print("Greetings!")

# while
a = 0

while a < 10:
    print('Hello')
    a += 1

# break
for i in range(10):
    print(i)

    if i == 5:
        break

# continue
for i in range(50):

    if i % 5 == 0:
        continue

    print(i)

# pass
for i in range(5):

    if i > 3:
        # do something later
        pass

# loop...else
for i in range(5):
    print(i)
else:
    print("Success!")  # calls the else block once the last loop exits successfully
