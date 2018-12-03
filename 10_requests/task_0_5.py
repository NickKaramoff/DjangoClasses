import requests

link = 'https://karamoff.ru/conspects/style.scss'

response = requests.get(link)

f = open(link.split('/')[-1], 'wb')
f.write(response.content)
f.close()
