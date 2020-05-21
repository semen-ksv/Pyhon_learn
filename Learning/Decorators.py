from datetime import datetime
import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Считает время работы функции
        """

        print('Начало работы декоратора')
        start = datetime.now()
        print('Начало работы функции')
        result = func(*args, **kwargs)
        print('Окончание работы функции')
        print(datetime.now() - start)
        print('Окончание работы декоратора')
        return result

    return wrapper


def decorator1(arg):
    print(arg)  # если декоратор принимает аргументы
    def outer(func):  # функция передаеться дальше в фукнуию
        def wraper(*args, **kwargs):
            """
            Считает время работы функции
            """

            print('Начало работы декоратора')
            start = datetime.now()
            print('Начало работы функции')
            result = func(*args, **kwargs)
            print('Окончание работы функции')
            print(datetime.now() - start)
            print('Окончание работы декоратора')
            return result

        return wraper

    return outer


@decorator
def one(n):
    """some description"""
    list = []
    for i in range(n):
        if i % 2 == 0:
            list.append(i)
    print(len(list))
    return list


@decorator1('name')
def two(n):
    list = [x for x in range(n) if x % 2 == 0]
    print(len(list))
    return list


one(10)
print(one.__name__)
two(100000)
