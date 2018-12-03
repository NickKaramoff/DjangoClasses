import requests

link = 'https://karamoff.ru/conspects/style.scss'

response = requests.get(link)

f = open(link.split('/')[-1], 'w')
f.write(str(response.text))
f.close()
