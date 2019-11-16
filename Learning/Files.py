

# inputfile = 'Name.txt'
#
# myfile = open(inputfile, mode='r')

# print(myfile.read())

# for line in myfile:
#     print('Hello ' + line.strip())

# for num, line in enumerate(myfile, 1):      # переменная num номеруеться с "0". добавив к файлу начинает с 1
#     if 'Dandy' in line:
#         print('Line №' + str(num) + ': ' + line.strip())


# paroly = 'Paroly.txt'
# myfile3 = open(paroly, mode='r')
#
# parol = 'Paroli.txt'
# myfile2 = open(parol, mode='a')
#
# pasw_find = 'hoches'
#
# for num, line in enumerate(myfile3, 1):
#     if pasw_find in line:
#         print('Line №' + str(num) + ': ' + line.strip())     # line.strip обрезает пробелы и переносы
#         # записать в myfile2 найденые линии
#         myfile2.write("Found pasvords: " + line)
#
# myfile2.close()
# # myfile.close()
# myfile3.close()


list1 = ['good', 'bad', 'real', 'strong']
list2 = ['white', 'red', 'bad']
list3 = []

for x in list1:
    if all(x != y for y in list2):
        list3.append(x + '\n')

print(list3)

f1 = open('List.txt', 'r+', encoding='utf_8')
c = f1.read()
print('-------------')
print(c, end='')
print('-------------')
for word in list3:
    if word not in c:
        # f1 = open('List.txt', 'a', encoding='utf_8')
        f1.write(word)
        print(word)

print('-------------')
print(c, end='')
print('-------------')
f1.close()
