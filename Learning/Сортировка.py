from random import randint
import time

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 5, 1, 7, 3, 9, 8, 6, 4]
c = [9, 8, 7, 6, 5, 4, 3, 2, 1]
g = [randint(0, 1000) for p in range(10000)]

sorted(g)        # 0.319335452, 0.309540058, 0.317734711

"""
Bubble Sort
совершается несколько проходов по массиву. 
При проходе последовательно сравниваются пары элементов в массиве 
и в случае несоответствия выбранному порядку меняются местами. 
Если пары элементов находятся в верном порядке, то ничего не происходит. 
В результате первого прохода максимальный элемент окажется в конце, 
nо есть всплывет словно пузырек. Затем все повторяется до того момента 
пока весь массив не будет отсортирован.
"""
def sort(arr):      # 29.865360011, 30.264031712, 30.131153292
    while True:
        cerrected = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                cerrected = True
        if not cerrected:
            return arr

"""
Сортировка выбором 
чтобы отсортировать массив, находим элемент с минимальным значением,
затем сравниваем его со значением первой неотсортированной позиции. 
Если этот элемент меньше, то он становится новым минимумом и их позиции меняются.
"""

def ssort(array):       #  8.092554187, 8.170902884, 8.147274854
    for i in range(len(array)):
        indxMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return a

"""
Сортировка вставками
из массива последовательно берется каждый элемент
вставляется в его отсортированную часть(например в начале массива)
"""
def isort(array):       #  10.909419106, 11.040589566, 10.763806735
    for i in range(len(array)):
        v = array[i]
        j = i
        while (array[j-1] > v) and (j > 0):
            array[j] = array[j-1]
            j = j - 1
        array[j] = v

    return array

"""
Сортировка Шелла 
просматриваються элементы беря каждый i тый элементы(начало откуда угодно). 
В результате мы получаем массив где каждый i-тый элемент отсортирован. 
Повторяя такую операцию с использованием меньших i, заканчивая 1 результатом будет 
отсортированный массив.
"""
def Shell(A):           #  2.633587986, 2.734006739, 2.633260007
    t = int(len(A)/2)
    while t > 0:
        for i in range(len(A)-t):
            j = i
            while j >= 0 and A[j] > A[j+t]:
                A[j], A[j+t] = A[j+t], A[j]
                j -= 1
        t = int(t/2)
    return A

"""
Быстрая сортировка
выбирается опорный элемент, относительно которого будет происходит сортировка. 
Равные и бОльшие элементы помещаются справа, меньшие – слева. 
Затем к полученным подмассивам рекурсивно применяются два первых пункта.
"""
def QuickPas(s, aL, aR):
    l, r = aL, aR
    mid = (s[l]+s[(l+r)/2]+s[r])/3
    while mid:
        r-=1
        if l<=r:
            if s[l]>s[r]:
                s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
    if r>aL: QuickPas(s, aL, r)
    if l<aR: QuickPas(s, l, aR)

def qsort(inlist):      #  0.410480746, 0.35482674, 0.360837577, 0.334424287
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


print(sorted(a))
print(sorted(b))
print(sorted(c))
print(sorted(g))
print(time.clock())
