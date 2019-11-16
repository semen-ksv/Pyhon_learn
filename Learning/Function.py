def print_prev(name):
    print('Congrarulanion', name + ' Wish you oll the best')
    print('Hello')

def sum(x, y):
   s = x + y
   return s

print_prev('Sem')

sum(4, 5)
x = sum(3, 5)
print(x)


#1! = 1*2
#2! = 1*2*3
def factorial(x):
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i
    return otvet

f = factorial(3)
print(f)

for i in range(1, 10):
    print(str(i) + '! = ' + str(factorial(i)))

#------------------------------------------------------
print('########################################')

def create_record(name, tel, adres):
    record = {
        'name': name,
        'phone': tel,
        'adress': adres
    }
    return record

user1 = create_record('Sem', '34434', 'Riga')
user2 = create_record('Jon', '95775', 'London')

print(user1, user2)

def giv_award(medal, *persons):
    for person in persons:
        print('Tovaish ' + person.title() + ' nagrajdaetsiy medal ' + medal)

giv_award('za belin', 'Sem', 'Petya')

#=======FACTORIAL====TIME===================

from functools import reduce
import time
import math
result = reduce(lambda x, y: x + y, range(1, 1000000))
print(result)

def timeit(func):
    def inner(x):
        start = time.time()
        func(x)
        end = time.time()
        print(end - start)
    return inner

@timeit
def factorial(x):
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i

    print(otvet)
    return otvet

f = factorial(100000)   # 24.863847017288208


@timeit
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(100000))    # 25.188090562820435


start = time.time()
res = reduce(lambda x,y: x * y, range(1, 100000))
print(res)
print(time.time() - start)  # 24.814642906188965


start1 = time.time()
print(math.factorial(100000))
print(time.time() - start1)  # 15.458784341812134

