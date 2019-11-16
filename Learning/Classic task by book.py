import time

def timeit(func):
    def inner(x):
        start = time.time()
        func(x)
        end = time.time()
        print(end - start)
    return inner

"""
Classic Computer Science Problem5 in Pyttton
Кnассическе аадачи
"""

#=========FIBONACHI=====================================================
some = 20
@timeit
def fib(num:int):
    a, b = 0, 1
    for i in range(0, num):
        a, b = b, a + b
    print(a)
fib(10000)

@timeit
def fib1(n:int):
    a = b = 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    print(a)
fib1(10000)

start = time.time()
def fib2(n:int):
    if n >= 2:
        return fib2(n-2) + fib2(n-1)
    else:
        return n
print(fib2(some))
end = time.time()
print(end - start)


start1 = time.time()
def fib3(n: int):
    memo = {0: 0, 1: 1}  # базовые случаи
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # мемоизация
    return memo[n]
print(fib3(some))
end1 = time.time()
print(end1 - start1)

def fib4(n: int):       # ГЕНЕРАТОР
    yield 0 # специальный случай
    if n > 0: yield 1 # специальный случай
    last: int = 0 #начальное значение fib(0)
    next: int = 1 #начальное значение fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # главный этап генерации
gen_fib = fib4(30)
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))


