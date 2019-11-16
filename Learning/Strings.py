name = "vasia puPkin"

print(name.title())     # первые заглавные
print(name.upper())     # все заглавные
print(name.lower())     # все маленькие

print('Messages:\n\tmessages1\n\tmessages2\n\tmessages3\nEND\n')  #перенос и табуляция
print("Lover name: " + name.lower())

log = ' . , Sem hoches ,, . '
print(log)

# убрать пробелы (справа, слева, обе)
print(log.rstrip())
print(log.lstrip())
print(log.strip())
print(log.strip(', .'))

print(log.strip('., ').lower())


print(log.capitalize()) # первая буква большая остальные маленькие

a_list = ['banch', 'st', 'words', 'random']
print(' '.join(a_list))

a_list_2 = log.split()
for i in a_list_2:
    print(i)

# Акроним
original_str = "convert_to_acronim: "
original_str = original_str.upper()
list_of_words = original_str.split('_')
for word in list_of_words:
    print(word[0], end="")

print(original_str)
print(list_of_words)

# проверить начинаеться ли елемент сроки, списка с " указанного символа"
if name.startswith('v'):
    print(f'Строка {name} начинаеться с V')

    # перевернуть строку
st = 'words'
up_st = st.upper()
print(up_st)
sp_st = up_st.split()
print(sp_st)
y = 1
for i in up_st:

    x = len(up_st) - y
    print(up_st[x], end='')
    y += 1

print('\n' + st[::-1])


# функции enumerate()
students = ('James', 'Andrew', 'Mark')
for i, student in enumerate(students, 1):
    print(i,  student, sep=') ')


#import StrigIO - позволяет работать со строкой как с файлом

name = "vasia puPkin"
name.count('a')
print(name.count('a'))

print(name.center(33, '='))

print(name.isalnum())
print(name.isalpha())
print(name.islower())
print(name.isupper())
print(name.isspace())
print(name.istitle())

print(name.endswith('n'))   #проверка последнего символа
