import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

for text in soup.find_all('ol li article.product_pod h3 a'):
    print(text)

print(soup.find('ol li article.product_pod h3 a'))


response = requests.get('https://httpbin.org/#/Auth//basic-auth/{user}/{passwd}', auth=('user', 'passwd'))
print(f'Response content {response.content}')
print(f'Code {response.status_code}')
print(f'Text {response.text}')
# print(f'Json {response.json()}')

payload = {'key1': 'value1', 'key2': 'value2'}
response_with_data = requests.post('https://httpbin.org/post', data=payload)
print(response_with_data.headers)
print(response_with_data.text)
print(response_with_data.content)
print(response_with_data.status_code)