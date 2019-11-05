import requests
from bs4 import BeautifulSoup
import time
import webbrowser

head = {'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


def get_html(head, url):
    """Запрос к серверу по url сайта который укажем
        код 200 подтверждает что все работает
        свойство text вернет весь текст - код html сайта"""
    session = requests.Session()

    request = session.get(url, headers=head)
    return request.text


def get_pages_tex(html):
    """Обработка текста кода сайта и выделение названия законопроектов,
        вернем список законопроектов"""
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('table', class_="striped Centered")
    text_web = pages.find_all('td', align="left")

    _all_text = []

    for name_law in text_web:
        text_law = str(name_law).lstrip('<td align="left" valign="CENTER" width="60%">').rstrip('</td>')
        _all_text.append(text_law.strip() + '\n')
    return _all_text


def write_file(finded_text):
    """Запись найденого текста законопроектов в файл"""
    file = open('New bill.txt', 'r+', encoding='utf_8')
    read_file = file.readlines()
    for new_bill in finded_text:
        if all(new_bill.strip() != old_bill.strip() for old_bill in read_file):
            file.write(new_bill.strip() + '\n')
    file.close()


def main():
    rada_url = 'http://w1.c1.rada.gov.ua/pls/zweb2/webproc555'

    search_words = ['лотерея', 'лотереї', 'лотерей', 'лотерейної'
                    'азартний', 'азартні', 'азартних', 'азартної'
                    'гральний', 'грального', 'гральним', 'гральному']

    text_page = get_pages_tex((get_html(head, rada_url)))

    write_file(text_page)

    for word in search_words:
        if any(word in name_bill for name_bill in text_page):
            webbrowser.open('http://w1.c1.rada.gov.ua/pls/zweb2/webproc555')

            for word in search_words:
                for name_bill in text_page:
                    if word in name_bill:
                        print('Найден законопроект со словом: ' + word.upper() + ' в ' + name_bill)


    # ---------------альтернативный поиск-----------------
    # ----------------------1)
    # import re
    # word_lot = r'земель'
    # find_word = re.findall(word_lot, text_page)
    # print(f'Найдено {len(find_word)} слов - {find_word}')

    # ----------------------2)


if __name__ == '__main__':
    while True:
        main()
        print('.')
        time.sleep(600)

    # автозапус реализовать через bat файл
    # директороия для файла C:\Documents and Settings\All Users\Start Menu\Programs\Startup

