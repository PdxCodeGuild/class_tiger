import requests
from bs4 import BeautifulSoup

''' gets the content from the local server port 8000 and does stuff '''

r = requests.get('http://0.0.0.0:8000/')
# print(r.content)
soup = BeautifulSoup(r.content,"lxml")
# paragraph = soup.find_next('p','class:select_paragraph')

paragraphs = soup.find_all('p')

print(paragraphs)
