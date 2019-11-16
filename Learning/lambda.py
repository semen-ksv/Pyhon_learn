import time

start_time = time.time()


def funk(arg, arg1):
    result = arg * arg1
    return result


def funk1(arg, arg1):
    return arg * arg1

c = lambda arg, arg1: arg*arg1

print(c(5, 9))

for i in range(1300):
    print(i**i)

# сколько времени прошло при выполнении кода
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)