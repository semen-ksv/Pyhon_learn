
def fib():
    """
    :return: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fi = fib()
for i in range(20):
    print(next(fi))

def fibonacci_v4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return


for val in fibonacci_v4():
    print(val)


import random
def ret():
    yield random.randint(1,10000000)

print(next(ret()))
print(next(ret()))


def ret1(x):
    a = 0
    while a < x:
        yield a
        a += 1


print(list(ret1(10)))

def ref2(funk, x):
    for i in x:
        yield funk(i)

print(list(ref2(lambda x:x*2, [1,2,3,4])))


def zipf(a,b):
    i = 0

    while i < len(a) and i < len(b):
        yield (a[i], b[i])
        i += 1

print(list(zipf('abcd', [1,2,3,4])))
print(dict(zipf('abcd', [1,2,3])))


#---Прием значений с помощью метода send --------------
def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value is not None:
            data.append(new_value)

shop_queue = queue('Sem', "Bob", 'Jen', 'Karl')
for name in shop_queue:
    print(f'Please enter {name}')
    if name == 'Jen':
        print('Who are last?')
        name = shop_queue.send('Ann')
        print(f'Next enter {name}')


def generate(number):
    i = 0
    while i < number:
        yield i
        i += 1

g = generate(10)
print(list(g))

class Generator:
    def __init__(self, finish):
        self.number = 0
        self.finish = finish

    def __next__(self):
        if self.number < self.finish:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

mg = Generator(10)
print(next(mg))


# for i in mg:
#     print(i)

print(sum(mg))