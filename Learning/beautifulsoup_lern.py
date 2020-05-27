from bs4 import BeautifulSoup

sup_uhtm = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>This is a title</h1>
<p class="subtitle"> Loren some text</p>
<p>Here's announcer p without a class</p>
<ul>
    <li> Rolf </li>
    <li> Char </li>
    <li> Jen </li>
</ul>
</body>
</html>"""

simple_soup = BeautifulSoup(sup_uhtm, 'html.parser')

def find_title(name):
    title = simple_soup.find(name)
    print(title.string)

def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [x.string.strip() for x in list_items]
    print(list_contents)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    othe_paragraph = [p.string for p in paragraphs if 'subtitle' not in str(p)]
    # othe_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(othe_paragraph)

find_title('h1')
find_list_items()
find_subtitle()
find_other_paragraph()

