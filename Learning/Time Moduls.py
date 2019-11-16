import datetime

t = datetime.time(5, 32, 4, 12)
start = datetime.datetime.now()
print(t)
print(t.microsecond)
print(start)
print(datetime.time.max)
print(datetime.time.min)

day = datetime.date.today()
print(day)
print(day.timetuple())
print(day.day, day.month, day.year)

import timeit
start_time = timeit.default_timer()

a = '-'.join(str(n)for n in range(1000))
print(a)
print(timeit.timeit(str(a), number=10000))
b = '-'.join([str(n)for n in range(1000)])
print(timeit.timeit(str(b), number=10000))
c = '-'.join(map(str, range(1000)))
print(timeit.timeit(str(c), number=10000))
print(timeit.timeit(c, number=10000))

print(timeit.main())
print(timeit.default_timer() - start_time)