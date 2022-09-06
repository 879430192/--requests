import requests
from lxml import etree

url = 'https://fanqienovel.com/'

result = requests.get(url)

# print(result.text)
html = etree.HTML(result)
