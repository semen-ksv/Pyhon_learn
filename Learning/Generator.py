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