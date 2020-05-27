from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Bob', 'Jose', 'Anna', 'Jen', 'Sem'))

"""def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

def greet(g):
    yield from g

"""

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print("Finishing...")

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, word! Multitasking...')
greeter.send('How are you, ')
greeter.send('How are you, ')
greeter.send('How are you, ')
greeter.send('How are you, ')
greeter.send('How are you, ')
greeter.send('How are you, ')