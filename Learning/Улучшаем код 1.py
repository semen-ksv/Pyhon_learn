#1--------------------------------------------------
cities = ['Lviv', 'Kyiv', 'Odessa', 'Rivne']
#i = 0
#for city in cities:
#  print(i, city)
#  i += 1
  
# Good coding
for i, city in enumerate(cities):
  print(i, city)

#2---------------------------------------------------
x_list = [1, 2, 3]
y_list = [4, 5, 6]

for j in range(len(x_list)):
  x = x_list[j]
  y = y_list[j]
  print(x, y)
  
# Good coding
for x, y in zip(x_list, y_list):
  print(x, y)
  
#3-----------------------------------------------------
a = 6
b = 8
print('Befor: a = %d, b = %d' % (a, b))
tmp = a
a = b
b = tmp
print('Now: a = %d, b = %d' % (a, b))

#Good coding
a, b = 10, 15
a, b = b, a
print('Now: a = %d, b = %d' % (a, b))

#4--------------------------------------------------------
ages = {
  'Mary': 28, 
  'Jon': 31,
  'Simon': 18
}

if 'Simon' in ages:
  age = ages['Simon']
else:
  age = 'Unknown'
print('Simon is %s years old' % age)

#Good coding
age1 = ages.get('Simon', 'Unknown')
print('Simon is %s years old' % age1)

#5---------------------------------------------------------
need = 'b'
haystack = ['a', 'b', 'c', 'd', 'f']

found = False
for latter in haystack:
  if need == latter:
    print('Found')
    found = True
    break
if not found:
    print('Not found')
    
#Good coding1
for latter in haystack:
  if need == latter:
    print('Found')
    break
else:
    print('Not found')
    
#Good coding2  
print('Found' if need in haystack else 'Not found!')

#6-------------------------------------------------------
print('Coverting:')
x = input('input x: ')
try:
  print(int(x))
# except:
#   print('Converting fols')    #если нужно выполнить Доне используем Трай
finally:
  print('Done!')

#7----------------------------------------------------
a = 'Sem'
b = 'Happy'
c = f'Hello {a}!\nWhay are you {b}?'
print(c)
print('Hello', a+'!\nWhy are you', b+'?')
print('Hello {}!\nWhy are you {}?'.format(a, b))

#8------------------------------------------------------
#FizzBuzz
for i in range(1, 100+1):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 5 == 0:
    print('Buzz')
  elif i % 3 == 0:
    print('Fizz') 
  else:
    print(i)

#9------------------------------------------------------
#Fibonacci Sequence
a, b = 0, 1
for i in range(0, 10):
  print(a)
  a, b = b, a + b
  
#10------------------------------------------------------
#Generator| Comprehensions
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [a*a for a in my_list]
print(x)

#11------------------------------------------------------
#Fibonacci Generator

def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a+b

for item in fib(10):
    print(item)

#12---OOP bacik------------------------------------------
class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print('My name is {}'.format(self.name))

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print('...And I am {}'.format(self.hero_name))

corey = Person('Corey')
corey.reveal_identity()

superG = SuperHero('Corey', "BadMan")
superG.reveal_identity()
