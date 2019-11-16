
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
