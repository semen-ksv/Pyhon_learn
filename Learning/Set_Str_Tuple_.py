# a = (3, 3, 4, 5, 16, 43, 1, 2, 34, 5, 5, 3, 1)
# b = {3, 3, 4, 5, 16, 43, 1, 2, 34, 5, 5, 3, 1}
# print(a)
# print(len(a))
# print(b)
# print(len(b))
# w = ()
# f = {}
# g = []
# print(type(w))
# print(type(f))
# print(type(g))
from typing import TextIO

first = 'start'
second = 'finish'

q = first[::-1]
print(q)
w = first + second
print(w)
print(len(w))
c = first.__add__('foo')
c1 = first.join("bbb")
print(c)
print(c1)
print(c1[:5])
print(c1[3:7])
print(c1[::4])
print(c1.split("t"))

x = 'good'
print('place hea: %12.22s' % (x))
print('first: {b}, second: {b}'.format(b=12))

my_list = [1, 2, 2, 3, 4, 2]
print(my_list[1:3])
new_list = my_list[2] = 15
print(new_list)
print(my_list)

rr = my_list.count(2)
print(rr)
sort_list = my_list.sort()
rew_list = my_list.reverse()
print(sort_list)
print(rew_list)

print(my_list)

d_f: TextIO = open('test')
d_f.read()
d_f.seek(0)
fff = d_f.readline()
print(fff)

s_set = [1, 2, 3, 3, 4, 5, 6, 6, 6]
l_set = set(s_set)
m_set = list(l_set)
print(l_set)
print(m_set)

# генератор списка
comp_list = [x for x in range(5)]
comp_l = [r for r in 'world']
comp_r = [x**2 for x in range(1, 11)]
print(comp_r)
print(comp_l)
print(comp_list)

lst = [num for num in range(10) if num % 2 == 0]
print(lst)

list_in_list = [x**2 for x in[x**2 for x in range(11)]]
print(list_in_list)


st = 'second time l  will relaks go to the school at six o'

for t in st.split():
    if t[0] == 's':
        print(t)
sr_comp = [word[0] for word in st.split()]
print(sr_comp)

help(st.format)
st.format()


list1 = ['good', 'bad', 'real']
list2 = ['white', 'red', 'bad']

res = [x for x in list1 if x in list2]
print(res)

list3 = []
for x in list1:
    if all(x != y for y in list2):
        list3.append(x + '\n')
        print(x)
print(list3)


list4 = []
for x in list1:
    if x not in list2:
        list4.append(x)
        print(x)
print(list4)

