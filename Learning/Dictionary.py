
#       (-----item-----)
#       [key]    [value]

enemy = {'loc_x': 70,
         'loc_y': 50,
         'color': 'gren',
         'health': 100,
         'name': 'Miho',
         'awards': ('za pobedy', 'gerow'),
         'image': ['image1.jpg', 'image2.jpg']
         }

print(enemy)

print('Location X = ' + str(enemy['loc_x']))
print('Location Y = ' + str(enemy['loc_y']))
print('His name is: ' + enemy['name'])

enemy['rank'] = 'Kapitan'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())
# enemy.pop(1)
# enemy.popitem()
# enemy.items() #возвращает колекцию ключ, пара



all_enemis = [] # новый масив и добавление в него словарей


for x in range(5):
    all_enemis.append(enemy.copy())


all_enemis[4]['health'] = 30
all_enemis[2]['name'] = 'Gogi'
all_enemis[1]['loc_x'] += 10

for en in all_enemis: # распечатать списком
    print(en)



d = {}
for i in "lsjdfiejfsadfoisjdf":
    # if i in d:
    #     d[i] += 1
    # else:
    #     d[i] = 1
    d[i] = d.get(i, 0) + 1  # то же самое что и верхний код
print(d)

for i in sorted(d):  #  отсортировать и вывести отдельно каждую позицию словаря
    print(i, d[i])

d = {'a': 1, 'b': 2}
ql = dict(zip(d.values(), d.keys()))
print(ql)


a = ['vova_333', 'dima_222', 'sem_888']
b = {}
c = []
w = []
for i in a:
    av, ab = i.split('_')
    b.setdefault(av, ab)
    c.append(av)
    w.append(ab)
    nd = dict(zip(c,w))
    print(b)
    print(c)
    print(w)
    print(nd)


ddd = {'k1': 1, 'k2': 2}
ccc = {x: x**2 for x in range(10)}
print(ccc)
for ki in ddd.items():
    print(ki)
    print(ki[0], ki[1])

print(ddd.values())
print(ddd.keys())