import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

print(soup.title.get_text())
print(response.status_code)

tds = []
for tr in soup.find_all('tr'):
    tds.extend(tr.find_all('td'))

print(tds)