import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
fogi@coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern1 = re.compile(r'[^b]at', re.I)

matches = pattern1.search(text_to_search)

find = re.findall(r'[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9_.+-]+\.+[a-zA-Z0-9]+', text_to_search)
print(matches)
print(text_to_search[0:5])
print(find)

print(r'\tTab') # сохраняет строку так как она написана и \t не выполняеться


(r'start', re.IGNORECASE) # поиск независимо какие большие или маленькие буквы!!!

"""
Оператор	Описание
.	    Один любой символ, кроме новой строки \n.
?	    0 или 1 вхождение шаблона слева             (r'https?://(www\.)?\w+\.\w+') - поиск доменного имени
+	    1 и более вхождений шаблона слева
*	    0 и более вхождений шаблона слева

\w  	Любая цифра или буква 
\W      все, кроме буквы или цифры
\d      Любая цифра [0-9]                           \d\d\d.\d\d\d.\d\d.\d\d  телефон 050-415-99-32
\D      все, кроме цифры)
\s	    Любой пробельный символ 
\S      любой непробельнй символ
\b	    Граница слова

[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
[1-9]   поиск всех входящих в группу
[a-z] [A-Z] [a-zA-Z] поиск всех входящих в группу
\	    Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{3}     точная цифра
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b 	Соответствует a или b
()	    Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
"""

"""
методы, которые предоставляет библиотека re:

re.match(pattern, string)   ищет по заданному шаблону в начале строки
re.search(pattern, string)  ищет по всей строке, но возвращает только первое найденное совпадение - быстрее
re.findall(pattern, string) возвращает список всех найденных совпадений!!!
re.split(pattern, string, [maxsplit=0]) разделяет строку по заданному шаблону.
re.sub(pattern, repl, string)   ищет шаблон в строке и заменяет его на указанную подстроку
re.compile(pattern, repl, string) собирает регулярное выражение в отдельный объект, который может быть использован для поиска.
"""


patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other'
re.search('hello', 'Jim hello dude')   #виводит адрес совпадения

for pattern in patterns:
    print(f'Searching for {pattern} in: \n {text}')
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No match was found')


split_term = '@'

phrase = 'What is your email, is hello@word.com'

c = re.split(split_term, phrase)
print(c)
b = phrase.split('@')
print(b)

'''удалить пунктуацию со строки'''
strings = 'This is a string! But, it has punctuation. How can yuo remove them?'

rem_punct = re.findall('[^!.?, ]+', strings)
print(rem_punct)

import requests
url = 'https://habrahabr.ru/'
r = requests.get(url).text
pattern = r'(http|ftp|https)://([\w-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
get = re.findall(pattern, r)
for i in get:
    print(i)
print(get)