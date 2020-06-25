a = [1, 2, 3, 4]
c = [i for i in a if i % 2 == 0]
b = (i for i in a if i % 2 == 0)
print(c)
print(list(q for q in b))
# =====================================================

from collections import Counter

l = [1, 1, 1, 2, 3, 3, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 9, 4, 5, 8, 9, 9, 9]
s = 'some some words in text text text'

print(Counter(l))
print(Counter(s.split()))

words = Counter(s.split())
print(words.most_common(3))
print(words.items())
print(sum(Counter(l)))
print(list(words))
print(set(words))
# =========================================================

from collections import defaultdict

d = {'k': 1}
print(d['k'])
w = defaultdict()  # defaultdict(lambda: 0) - словарь который присваевает ключам значение по умолчанию 0
w['p'] = 2
for i in w:
    print(i)
print(w)

goods = [
    ['meat', 22],
    ['bread', 10],
    ['milk', 2],
    ['meat', 5],
    ['bread', 7],
    ['milk', 12]
]

goods_count = defaultdict(int) # int или (lambda: 0)
for name, quantity in goods:
    goods_count[name] += quantity
print(goods_count)
# =========================================================

from collections import OrderedDict

'''словарь запоминает порядок в словаре в отличии от обычного словаря'''
t = OrderedDict()
t['a'] = 1
t['b'] = 2
t['x'] = 3
print(t)
# ==========================================================

from collections import namedtuple

'''кортеж которий позволяет присваивать имена своим полям'''
k = (1, 2, 3, 4, 5)
print(k[0])

Dog = namedtuple('Dog', 'age name breed')
sam = Dog(2, 'Sammy', 'Labrador')
guf = Dog(age=4, name='Guffy', breed='Spaniel')
print(sam)
print(sam.age)
print(sam[1])
print(guf.name)
