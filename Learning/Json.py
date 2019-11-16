import json
import requests
data = {'name': 'Sem', 'number': 123, 'ARE': 'qqqq'}
# file = open('some.json', 'a')
# file.write(data)
# file.close()

data1 = open('some.json', 'r')

obj = json.dumps(data, sort_keys=True, indent=4)
s = json.load(data1)
print(obj)
print(s)


url = 'https://jsonplaceholder.typicode.com/comments'
r = requests.get(url)
c = r.headers
print(c)
file = open('some.json', 'w')
for i in c.items():
    # print(i,'--',c[i])
    jfile = json.dumps(i)
    file.write(jfile + '\n')

file.close()