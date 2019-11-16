num = [1, 2, 3, 4, 5,  6, 7, 8, 9]
my_list =[]
#----------------------------------------------------------------------------
for n in num:
  my_list.append(n)
print(my_list)

my_list1 = [n for n in num]   #comprehention - генератор, аналогично верхнему
print(my_list1)
#----------------------------------------------------------------------------

my_list2 =[]
for n in num:
  my_list2.append(n*n)
print(my_list2)

my_list21 = [n*n for n in num]
print(my_list21)

my_list22 = list(map(lambda x: x*x, num))
print(my_list22)
#----------------------------------------------------------------------------

# функция – map - когда внезапно нужно применить какую-либо функцию к каждому элементу списка.
def f(x):
  return x*x

nums = [1, 2, 3]

for num in nums:
  print (f(num))

#Более опытный нуб изучивший list comprehensions :
def f(x):
  return x*x

print (list(f(num) for num in nums))

#Программист сделает проще :
def f(x):
    return x*x
print (list(map(f, nums)))

#А тру-мэдскиллз хакер сделает следующим образом (при условии конечно, что функцию можно записать лямбдой,
#далеко не всегда функция будет достаточно простой чтобы записать ее лямбдой) :

print (list(map(lambda x: x*x, nums)))
#----------------------------------------------------------------------------

my_list3 = []
for n in num:
  if n % 2 == 0:
    my_list3.append(n)
print(my_list3)

my_list31 = [n for n in num if n%2 == 0]
print(my_list31)

my_list32 = list(filter(lambda n: n%2 == 0, num))
print(my_list32)

#объеденить (1, 2, 3) и (a, b, c) попарно-------------------------------------
my_list4 =[]
for letter in 'abc':
  for i in range(1, 4):
    my_list4.append((letter, i))
print(my_list4)

my_list41 = [(letter, i) for letter in 'abc' for i in range(1, 4)]
print(my_list41)
#---------------------------------------------------------------------------

# Dictionary comprehensions
name = ['Bruse', 'Klark', 'Beil', 'Peter']
hero = ['Batmen', 'Superman', 'Spiderman', 'Dedpul']

print(list(zip(name, hero)))

# dict ('name': hero) для каждого героя в zip()
my_dict = {}
for name, hero in zip(name, hero):
  my_dict[name] = hero
print(my_dict)

my_dict1 = {name:hero for name, hero in zip(name, hero)}
print(my_dict1)

#if name not equal 'Peter'
my_dict2 = {name:hero for name, hero in zip(name, hero) if name != 'Peter'}
print(my_dict2)

# SET comprehention
nums = [1,1,2,1,3,4,4,5,6,7,8,8,8,9,5,7]
my_set = set()
for n in nums:
  my_set.add(n)
print(my_set)

my_set1 = {n for n in nums}
print(my_set1)