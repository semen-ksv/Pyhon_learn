class Car:

    def __init__(self):
        self.dor = 5
        self.window = 6
        self.whils = 4
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return f'{self.dor}'
        if self.i == 2:
            return f'{self.window}'
        if self.i == 3:
            return f'{self.whils}'
        if self.i == 4:
            return f'All car'
        raise StopIteration()


car = Car()
for value in car:
    print(value)


class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(10)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)