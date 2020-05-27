import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

for text in soup.find_all('ol li article.product_pod h3 a'):
    print(text)

print(soup.find('ol li article.product_pod h3 a'))