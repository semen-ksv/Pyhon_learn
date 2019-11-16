cities = ['New York', 'Kiev', 'moskov', 'tORONTO', 'Vishneve']

print(cities)

print(len(cities))
print(cities[2])
print(cities[-2])

print(cities[2].title(), cities[3].title())

cities[2] = 'Odessa'
print(cities)

cities.append('Lviv')
print(cities)

cities.insert(0, 'Riga')
print(cities)

cities.remove('Vishneve')   #стереть один раз
print(cities)

del cities[1]
print(cities)

deleted_city = cities.pop(0) # удалить по индексу, или последний
print('Deleted city is: ' + deleted_city)
print(cities)


cities.sort() # по афавиту
print(cities)

cities.reverse()
print(cities)

cars = ['Reno', 'BMW', 'Leon', 'VW', 'Seat']
print(cars)

for car in cars:
    print(car.upper())

for car in range(1, 6):
    print(car)

my_namber_list = list(range(10+1))
print(my_namber_list)

for x in my_namber_list:
    x = x * 2
    print(x)

my_namber_list.sort(reverse=True)
print(my_namber_list)

print('Max nam is: ', max(my_namber_list))
print('Min nam is: ', min(my_namber_list))
print('Summ of list is: ', sum(my_namber_list))

my_cars = cars[1:3]
print(my_cars)

you_cars = cars[:4]
print(you_cars)

our_cars = cars[0:5:2]
print(our_cars)

mycars = cars[:] #копия. при этом при изменении каждого будет независимо

if 'BMW' in cars:
    print("Bmw in list")

german_cars = ['BMW', 'VW']
# перебор по двух списках на соответсвие
for car in cars:
    if car in german_cars:
        print(car + ' is german car')
    else:
        print(car + ' isn\'t german car')

# удалить повторяющиеся элементы списка
lst = ["a", "b", "a", "c", "c"]
lst = list(dict.fromkeys(lst))
print(lst)

# функция фильтер и варианты записи без использования функции фильтер
def has_o(strings):
    return 'o' in strings.lower()

a_st = ['one', 'two', 'three', 'ten', 'zero']
b_st = list(filter(has_o, a_st))
c_st = list(filter(lambda string: 'o' in string.lower(), a_st))
d_st = [string for string in a_st if 'o' in string]
i_st = [string for string in a_st if has_o(string)]
print(b_st)
print(c_st)
print(d_st)
print(i_st)

dir(a_st)

nw_list = [1, 2, 3, 4, 5]
nw_list.append(6)
nw_list.count(2)
nw_list.append([7, 8])
nw_list.extend([9, 10, 11])
nw_list.insert(2, 'insert')
nw_list.pop()
nw_list.remove('insert')
nw_list.reverse()
nw_list.remove([7, 8])
nw_list.sort()
print(nw_list)

