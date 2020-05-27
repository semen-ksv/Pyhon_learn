import time
from multiprocessing import Process

#  использовать Process для задач которые требуют длительного выполнения одновременно
# не использовать для задач которые ожидают, так как они не выполняться при занятом процесе одним из длинных процесов

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello {user_input}!'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print('Started calculation....')
    [x**2 for x in range(20000000)]
    print(f'Complex calc. total time {time.time() - start}')

#
# start = time.time()
# ask_user()
# complex_calculation()
# print(f'Single thread total time {time.time() - start}')


process = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)

process.start()
process2.start()

start2 = time.time()


process.join()
process2.join()


print(f'Multiprocessing finish {time.time() - start2}')
