import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Food/index.html"

for i in range(5):
    print('第', i+1 , '頁')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find_all('div', class_="r-ent")
    for tag in tags:
        date = tag.find('div', class_='date').text
        info = tag.find('a').text
        print(date, info)
    links = soup.find_all('a', class_="btn wide")
    url = 'https://www.ptt.cc' + links[1].get('href')